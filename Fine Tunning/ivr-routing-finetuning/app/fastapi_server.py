import json
import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Pydantic models for request and response
class PredictionRequest(BaseModel):
    transcript: str
    intent: str

class PredictionResponse(BaseModel):
    series_of_commands: list

# Initialize FastAPI app
app = FastAPI(
    title="IVR Navigation Assistant",
    description="A fine-tuned LLM for predicting IVR navigation commands from transcript and user intent.",
    version="1.0.0"
)

# Global variables for model and tokenizer
model = None
tokenizer = None

def load_model():
    """Load the fine-tuned model and tokenizer."""
    global model, tokenizer
    adapter_path = "adapters"  # Relative to where the app is run
    base_model_name = "Qwen/Qwen3-8B-Instruct"

    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )

    model = PeftModel.from_pretrained(base_model, adapter_path)
    model.eval()
    print("Model loaded successfully!")

@app.on_event("startup")
async def startup_event():
    """Load model on startup."""
    load_model()

def extract_nav_commands(output_str: str):
    """Extract navigation commands from the model's output string."""
    try:
        data = json.loads(output_str.strip())
        return data.get("series_of_commands", [])
    except json.JSONDecodeError:
        # Try to find JSON in the string
        import re
        json_match = re.search(r'\{.*\}', output_str, re.DOTALL)
        if json_match:
            try:
                data = json.loads(json_match.group())
                return data.get("series_of_commands", [])
            except:
                pass
        return []

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Predict navigation commands for given transcript and intent."""
    global model, tokenizer

    if model is None or tokenizer is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    # Format input
    system_message = "You are an IVR navigation assistant."
    user_message = f"Transcript: {request.transcript} User Intent: {request.intent}"

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    # Apply chat template if available
    if hasattr(tokenizer, "apply_chat_template"):
        input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    else:
        input_text = f"<system>\n{system_message}\n</system>\n<user>\n{user_message}\n</user>\n<assistant>\n"

    # Tokenize
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512).to(model.device)

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
    commands = extract_nav_commands(generated_text)

    return PredictionResponse(series_of_commands=commands)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    if model is None or tokenizer is None:
        return {"status": "unhealthy", "detail": "Model not loaded"}
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)