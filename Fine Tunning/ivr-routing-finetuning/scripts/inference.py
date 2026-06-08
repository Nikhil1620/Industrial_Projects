import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

def load_model_and_tokenizer(adapter_path: str, base_model_name: str):
    """Load the fine-tuned model and tokenizer for inference."""
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

def predict_navigation(model, tokenizer, transcript: str, user_intent: str, max_length=512):
    """Predict navigation commands given transcript and user intent."""
    # Format input
    system_message = "You are an IVR navigation assistant."
    user_message = f"Transcript: {transcript} User Intent: {user_intent}"

    # Prepare messages
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    # Apply chat template if available
    if hasattr(tokenizer, "apply_chat_template"):
        input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    else:
        # Fallback formatting
        input_text = f"<system>\n{system_message}\n</system>\n<user>\n{user_message}\n</user>\n<assistant>\n"

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

    # Extract navigation commands
    # We assume the generated text contains the JSON we want
    try:
        # Find the JSON part - it should be the last part after the assistant's response
        # We'll try to parse the entire generated text as JSON, but it might have extra text.
        # Instead, we'll look for a JSON object in the string.
        import re
        json_match = re.search(r'\{.*\}', generated_text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            data = json.loads(json_str)
            return data.get("series_of_commands", [])
        else:
            return []
    except Exception as e:
        print(f"Error parsing output: {e}")
        return []

def main():
    # Configuration
    adapter_path = "adapters"  # Path to saved adapter
    base_model_name = "Qwen/Qwen3-8B-Instruct"

    print("Loading model and tokenizer...")
    model, tokenizer = load_model_and_tokenizer(adapter_path, base_model_name)

    # Example usage
    print("\n=== IVR Navigation Assistant ===")
    print("Enter 'quit' to exit")

    while True:
        transcript = input("\nEnter IVR transcript: ").strip()
        if transcript.lower() == 'quit':
            break

        user_intent = input("Enter user intent: ").strip()
        if user_intent.lower() == 'quit':
            break

        commands = predict_navigation(model, tokenizer, transcript, user_intent)
        print("\nPredicted navigation commands:")
        print(json.dumps({"series_of_commands": commands}, indent=2))

if __name__ == "__main__":
    main()