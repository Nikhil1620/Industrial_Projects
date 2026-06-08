import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
from datasets import load_dataset
from tqdm import tqdm
import numpy as np
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

def load_model_and_tokenizer(adapter_path: str, base_model_name: str):
    """Load the fine-tuned model and tokenizer."""
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    # Load base model
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )

    # Load the adapter
    model = PeftModel.from_pretrained(base_model, adapter_path)
    model.eval()

    return model, tokenizer

def extract_nav_commands(output_str: str):
    """Extract navigation commands from the model's output string."""
    try:
        # The output should be a JSON string: {"series_of_commands": [...]}
        data = json.loads(output_str.strip())
        return data.get("series_of_commands", [])
    except json.JSONDecodeError:
        # If parsing fails, return empty list
        return []

def evaluate_model(model, tokenizer, test_dataset, max_length=512):
    """Evaluate the model on the test dataset."""
    # Metrics
    exact_match_count = 0
    nav_accuracy_count = 0
    total_count = 0

    # For precision, recall, F1: we'll collect all true and predicted navValues
    true_labels = []
    pred_labels = []

    # Get all possible navValues from the dataset (for label encoding)
    # We'll extract from the test dataset
    all_nav_values = set()
    for example in test_dataset:
        # The ground truth is in the assistant's message
        messages = example["messages"]
        for msg in messages:
            if msg["role"] == "assistant":
                try:
                    data = json.loads(msg["content"])
                    for cmd in data.get("series_of_commands", []):
                        all_nav_values.add(cmd.get("navValue"))
                except:
                    pass

    # Convert to list for consistent ordering
    all_nav_values = sorted(list(all_nav_values))
    nav_to_id = {nav: idx for idx, nav in enumerate(all_nav_values)}
    id_to_nav = {idx: nav for nav, idx in nav_to_id.items()}

    # Iterate over test dataset
    for example in tqdm(test_dataset, desc="Evaluating"):
        # Format the input
        messages = example["messages"]
        # We need to remove the assistant's message for input
        input_messages = messages[:-1]  # Remove last assistant message

        # Apply chat template if available
        if hasattr(tokenizer, "apply_chat_template"):
            input_text = tokenizer.apply_chat_template(input_messages, tokenize=False, add_generation_prompt=True)
        else:
            # Fallback formatting
            input_text = ""
            for msg in input_messages:
                if msg["role"] == "system":
                    input_text += f"<system>\n{msg['content']}\n</system>\n"
                elif msg["role"] == "user":
                    input_text += f"<user>\n{msg['content']}\n</user>\n"
            input_text += "<assistant>\n"

        # Tokenize
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=max_length).to(model.device)

        # Generate
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=50,
                temperature=0.1,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
            )

        # Decode
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract the assistant's response (after the last assistant marker)
        # We'll try to find the JSON part
        # In our formatting, the assistant's response starts after the last <assistant>\n
        # But since we used the chat template, we can split by the tokenizer's eos token?
        # Instead, we'll look for the JSON pattern in the generated text.
        # We'll assume the generated text contains the JSON we want.

        # Extract navigation commands from generated text
        pred_commands = extract_nav_commands(generated_text)

        # Ground truth commands
        true_commands = []
        for msg in messages:
            if msg["role"] == "assistant":
                true_commands = extract_nav_commands(msg["content"])
                break

        # Exact match: compare the entire list of commands
        if pred_commands == true_commands:
            exact_match_count += 1

        # Navigation command accuracy: we compare the first command's navValue (assuming one command)
        # But we should handle multiple commands? In our dataset, we only have one.
        # We'll compute accuracy based on the first command if exists.
        if len(pred_commands) > 0 and len(true_commands) > 0:
            pred_nav = pred_commands[0].get("navValue")
            true_nav = true_commands[0].get("navValue")
            if pred_nav == true_nav:
                nav_accuracy_count += 1

            # For precision/recall, we consider each navValue as a class
            # We'll only consider the first command for simplicity
            if pred_nav in nav_to_id and true_nav in nav_to_id:
                pred_labels.append(nav_to_id[pred_nav])
                true_labels.append(nav_to_id[true_nav])
            else:
                # If the navValue is not in our set, we skip for precision/recall (or treat as unknown)
                pass
        elif len(pred_commands) == 0 and len(true_commands) == 0:
            # Both empty, consider as correct for nav accuracy?
            nav_accuracy_count += 1
            # For precision/recall, we skip because there's no label
        else:
            # One is empty and the other is not -> incorrect
            pass

        total_count += 1

    # Compute metrics
    exact_match_accuracy = exact_match_count / total_count if total_count > 0 else 0
    nav_accuracy = nav_accuracy_count / total_count if total_count > 0 else 0

    precision, recall, f1, _ = precision_recall_fscore_support(
        true_labels, pred_labels, average='weighted', zero_division=0
    )

    # Also compute accuracy for the classification task
    classification_accuracy = accuracy_score(true_labels, pred_labels) if true_labels else 0

    # Prepare report
    report = {
        "exact_match_accuracy": exact_match_accuracy,
        "navigation_command_accuracy": nav_accuracy,
        "classification_accuracy": classification_accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "total_samples": total_count,
        "exact_match_correct": exact_match_count,
        "navigation_correct": nav_accuracy_count,
    }

    return report

def main():
    # Configuration
    adapter_path = "adapters"  # Path to saved adapter
    base_model_name = "Qwen/Qwen3-8B-Instruct"

    print("Loading model and tokenizer...")
    model, tokenizer = load_model_and_tokenizer(adapter_path, base_model_name)

    print("Loading test dataset...")
    test_dataset = load_dataset("json", data_files="data/test.jsonl", split="train")

    print("Evaluating model...")
    report = evaluate_model(model, tokenizer, test_dataset)

    # Print report
    print("\n=== Evaluation Report ===")
    for key, value in report.items():
        if isinstance(value, float):
            print(f"{key}: {value:.4f}")
        else:
            print(f"{key}: {value}")

    # Save report to file
    with open("evaluation_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\nEvaluation report saved to evaluation_report.json")

if __name__ == "__main__":
    main()