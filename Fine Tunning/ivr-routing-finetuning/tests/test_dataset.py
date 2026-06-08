import os
import json
import subprocess
import sys

def test_dataset_generation():
    """Test that the dataset generation script runs and creates the expected files."""
    # Run the dataset generation script
    result = subprocess.run(
        [sys.executable, "scripts/prepare_dataset.py"],
        cwd=os.path.dirname(os.path.abspath(__file__)) + "/..",
        capture_output=True,
        text=True
    )

    # Check that the script ran successfully
    assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    # Check that the data files were created
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    assert os.path.exists(os.path.join(data_dir, "train.jsonl")), "train.jsonl not found"
    assert os.path.exists(os.path.join(data_dir, "validation.jsonl")), "validation.jsonl not found"
    assert os.path.exists(os.path.join(data_dir, "test.jsonl")), "test.jsonl not found"

    # Check that each file has the expected number of lines (approximately)
    # We expect 70 train, 15 validation, 15 test
    with open(os.path.join(data_dir, "train.jsonl"), "r") as f:
        train_lines = f.readlines()
    with open(os.path.join(data_dir, "validation.jsonl"), "r") as f:
        val_lines = f.readlines()
    with open(os.path.join(data_dir, "test.jsonl"), "r") as f:
        test_lines = f.readlines()

    # Allow a small tolerance due to random splitting
    assert len(train_lines) >= 65 and len(train_lines) <= 75, f"Expected ~70 train samples, got {len(train_lines)}"
    assert len(val_lines) >= 10 and len(val_lines) <= 20, f"Expected ~15 validation samples, got {len(val_lines)}"
    assert len(test_lines) >= 10 and len(test_lines) <= 20, f"Expected ~15 test samples, got {len(test_lines)}"

    # Check that each line is valid JSONL and has the expected structure
    for line in train_lines[:5]:  # Check first 5 lines
        data = json.loads(line)
        assert "messages" in data
        assert len(data["messages"]) == 3
        assert data["messages"][0]["role"] == "system"
        assert data["messages"][1]["role"] == "user"
        assert data["messages"][2]["role"] == "assistant"
        # Check that the assistant's content is a JSON string with series_of_commands
        assistant_content = data["messages"][2]["content"]
        commands_data = json.loads(assistant_content)
        assert "series_of_commands" in commands_data
        assert isinstance(commands_data["series_of_commands"], list)
        for cmd in commands_data["series_of_commands"]:
            assert "navType" in cmd
            assert "navValue" in cmd
            assert cmd["navType"] == "Press"

    print("All tests passed!")

if __name__ == "__main__":
    test_dataset_generation()