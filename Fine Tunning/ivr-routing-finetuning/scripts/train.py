import os
import yaml
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer

def load_config(config_path: str) -> dict:
    """Load training configuration from YAML file."""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def main():
    # Load configuration
    config = load_config("configs/training_config.yaml")

    # Set up quantization configuration for QLoRA
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=False,
    )

    # Load model and tokenizer
    model_name = config["model_name_or_path"]
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token  # Ensure pad token is set

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )

    # Prepare model for k-bit training
    model = prepare_model_for_kbit_training(model)

    # Configure LoRA
    lora_config = LoraConfig(
        r=config["lora_r"],
        lora_alpha=config["lora_alpha"],
        target_modules=config["target_modules"],
        lora_dropout=config["lora_dropout"],
        bias="none",
        task_type="CAUSAL_LM",
    )

    # Apply LoRA to model
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # Load dataset
    train_dataset = load_dataset("json", data_files="data/train.jsonl", split="train")
    val_dataset = load_dataset("json", data_files="data/validation.jsonl", split="train")

    # Define formatting function for SFTTrainer
    def formatting_func(example):
        # The dataset is already in chat format, we just need to return the text
        # SFTTrainer expects a single string per example
        # We'll concatenate the messages with appropriate tokens
        # But note: The model expects a specific chat format. We'll use the tokenizer's chat template if available.
        # However, for simplicity, we'll just return the concatenated string as per the original format.
        # Alternatively, we can use the tokenizer's apply_chat_template.
        # Since we are using a custom format, we'll use the tokenizer's chat template if it exists.
        # Let's check if the tokenizer has a chat template.
        if hasattr(tokenizer, "apply_chat_template"):
            return tokenizer.apply_chat_template(example["messages"], tokenize=False, add_generation_prompt=False)
        else:
            # Fallback: manually format
            formatted = ""
            for message in example["messages"]:
                if message["role"] == "system":
                    formatted += f"<system>\n{message['content']}\n</system>\n"
                elif message["role"] == "user":
                    formatted += f"<user>\n{message['content']}\n</user>\n"
                elif message["role"] == "assistant":
                    formatted += f"<assistant>\n{message['content']}\n</assistant>\n"
            return formatted

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir=config["output_dir"],
        per_device_train_batch_size=config["per_device_train_batch_size"],
        gradient_accumulation_steps=config["gradient_accumulation_steps"],
        learning_rate=config["learning_rate"],
        num_train_epochs=config["num_train_epochs"],
        logging_steps=config["logging_steps"],
        save_steps=config["save_steps"],
        eval_steps=config["eval_steps"],
        warmup_steps=config["warmup_steps"],
        lr_scheduler_type=config["lr_scheduler_type"],
        fp16=config["fp16"],
        bf16=config["bf16"],
        gradient_checkpointing=config["gradient_checkpointing"],
        max_grad_norm=config["max_grad_norm"],
        weight_decay=config["weight_decay"],
        optim=config["optim"],
        save_total_limit=config["save_total_limit"],
        report_to=config["report_to"],
        run_name=config["run_name"],
        seed=config["seed"],
    )

    # Initialize SFTTrainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        dataset_text_field="text",  # We will create a 'text' field using formatting_func
        max_seq_length=config["max_seq_length"],
        tokenizer=tokenizer,
        args=training_args,
        formatting_func=formatting_func,
        packing=False,  # Set to True if you want to pack multiple examples into one sequence (requires more memory)
    )

    # Start training
    trainer.train()

    # Save the final model and adapter
    trainer.save_model()
    tokenizer.save_pretrained(config["output_dir"])

    print("Training completed! Model saved to:", config["output_dir"])

if __name__ == "__main__":
    main()