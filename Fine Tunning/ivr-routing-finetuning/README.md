# IVR Navigation Assistant

A production-ready system for predicting IVR navigation commands using fine-tuned open-source LLMs (Qwen 3 8B Instruct or Llama 3.1 8B Instruct) with QLoRA.

## Project Overview

This system takes an IVR transcript and user intent as input and predicts the correct navigation commands (e.g., "Press 2") to reach the desired department in an IVR system. The model understands semantic meaning and does not rely on exact keyword matching.

## Project Structure

```
ivr-routing-finetuning/
├── data/
│   ├── train.jsonl
│   ├── validation.jsonl
│   └── test.jsonl
├── scripts/
│   ├── prepare_dataset.py   # Synthetic dataset generation
│   ├── train.py             # QLoRA training script
│   ├── evaluate.py          # Evaluation script
│   └── inference.py         # CLI inference script
├── configs/
│   └── training_config.yaml # Training hyperparameters
├── adapters/                # Saved LoRA adapters (after training)
├── app/
│   └── fastapi_server.py    # FastAPI deployment server
├── tests/                   # Unit tests (to be implemented)
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker container for deployment
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ivr-routing-finetuning
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dataset Generation

The project includes a script to generate synthetic training data with varied IVR transcripts and user intents.

To generate the dataset:
```bash
python scripts/prepare_dataset.py
```

This will create:
- `data/train.jsonl` (70 samples)
- `data/validation.jsonl` (15 samples)
- `data/test.jsonl` (15 samples)

Each sample follows the OpenAI chat format:
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are an IVR navigation assistant."
    },
    {
      "role": "user",
      "content": "Transcript: ... User Intent: ..."
    },
    {
      "role": "assistant",
      "content": "{\"series_of_commands\":[{\"navType\":\"Press\",\"navValue\":\"2\"}]}"
    }
  ]
}
```

## Training

We use QLoRA (Quantized Low-Rank Adaptation) for efficient fine-tuning.

### Configuration

Training hyperparameters are configured in `configs/training_config.yaml`:
- Base model: Qwen/Qwen3-8B-Instruct
- Quantization: 4-bit with nf4
- LoRA: r=16, alpha=32, dropout=0.05
- Target modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- Batch size: 4 (with gradient accumulation)
- Learning rate: 2e-4
- Epochs: 3

### Start Training

```bash
python scripts/train.py
```

The trained adapter will be saved to the `adapters/` directory.

## Evaluation

Evaluate the fine-tuned model on the test set:

```bash
python scripts/evaluate.py
```

This computes:
- Exact Match Accuracy
- Navigation Command Accuracy
- Precision, Recall, F1 Score
- Classification Accuracy

Results are printed to console and saved to `evaluation_report.json`.

## Inference

Run inference on custom inputs:

```bash
python scripts/inference.py
```

Enter transcript and user intent when prompted, or integrate the `predict_navigation` function into your application.

Example:
```
Transcript: "Thank you for calling Coca-Cola. Press 1 for Orders. Press 2 for Equipment Service. Press 3 for Payments."
User Intent: "My vending machine is broken."

Output:
{
  "series_of_commands": [
    {
      "navType": "Press",
      "navValue": "2"
    }
  ]
}
```

## Deployment

### FastAPI Server

Start the API server:
```bash
python app/fastapi_server.py
```

The server will be available at `http://localhost:8000`.

Endpoint: `POST /predict`
```json
{
  "transcript": "Thank you for calling Coca-Cola. Press 1 for Orders. Press 2 for Equipment Service. Press 3 for Payments.",
  "intent": "My vending machine is broken."
}
```

Response:
```json
{
  "series_of_commands": [
    {
      "navType": "Press",
      "navValue": "2"
    }
  ]
}
```

### Docker Deployment

Build and run the Docker container:
```bash
docker build -t ivr-routing-assistant .
docker run -p 8000:8000 ivr-routing-assistant
```

## Model Improvements

To improve robustness and performance, consider:
1. **Data Augmentation**: Generate more diverse paraphrases of user intents using LLMs or back-translation.
2. **Synonym Expansion**: Use WordNet or embedding-based similarity to expand intent mappings.
3. **Prompt Engineering**: Experiment with different prompt formats and few-shot examples.
4. **Class Balancing**: Ensure balanced representation of all navigation options in training data.
5. **Error Analysis**: Analyze mispredictions to identify patterns and add targeted training examples.

## Experiment Tracking

We integrated Weights & Biases and TensorBoard for experiment tracking:
- Enable in `training_config.yaml` by setting `report_to: ["wandb", "tensorboard"]`
- Set up W&B account and run `wandb login` before training
- Launch TensorBoard: `tensorboard --logdir=runs`

## Production Considerations

For production deployment, consider:
1. **Hallucination Prevention**: Use constrained decoding or post-validation to ensure output is valid JSON.
2. **Confidence Scoring**: Extract generation scores to threshold low-confidence predictions.
3. **Fallback Routing**: Default to human operator or menu repetition when confidence is low.
4. **Human Escalation**: Provide option to speak to agent when navigation fails.
5. **Monitoring**: Track prediction latency, error rates, and drift in user intents.
6. **Logging**: Log all inputs and outputs for auditing and continuous improvement.
7. **Scaling**: Deploy behind a load balancer with autoscaling based on traffic.
8. **Security**: Implement authentication and rate limiting for the API endpoint.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Qwen team for the Qwen 3 series
- Hugging Face for transformers, peft, trl, and datasets
- The FastAPI and Uvicorn teams