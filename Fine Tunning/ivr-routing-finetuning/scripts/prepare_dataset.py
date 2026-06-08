import json
import random
from typing import List, Dict, Any

# Define IVR transcripts (menu options)
IVR_TRANSCRIPTS = [
    "Thank you for calling Coca-Cola. Press 1 for Orders. Press 2 for Equipment Service. Press 3 for Payments.",
    "Hello, you've reached TechSupport Inc. Press 1 for Software Issues. Press 2 for Hardware Repair. Press 3 for Account Management.",
    "Welcome to BankCorp. Press 1 for Checking Accounts. Press 2 for Savings Accounts. Press 3 for Loans. Press 4 for Credit Cards.",
    "Thanks for calling TravelCo. Press 1 for Flight Bookings. Press 2 for Hotel Reservations. Press 3 for Car Rentals. Press 4 for Cancellations.",
    "Greetings from HealthPlus. Press 1 for Appointments. Press 2 for Prescription Refills. Press 3 for Billing Inquiries. Press 4 for Emergency Services.",
]

# Define intent to navigation mapping with synonyms
INTENT_MAPPING = {
    # Coca-Cola
    "Orders": {
        "transcript_index": 0,
        "nav_value": "1",
        "synonyms": [
            "I want to place an order",
            "I need to buy products",
            "I want to purchase items",
            "I need to order supplies",
            "I want to make a purchase",
            "I need to buy beverages",
            "I want to order drinks",
            "I need to get beverages",
            "I want to buy soda",
            "I need to order soda"
        ]
    },
    "Equipment Service": {
        "transcript_index": 0,
        "nav_value": "2",
        "synonyms": [
            "My vending machine is broken",
            "I need equipment repair",
            "My machine is not working",
            "I need service on my equipment",
            "My vending machine needs fixing",
            "I have an equipment issue",
            "My machine is broken",
            "I need technical support for equipment",
            "My vending machine is malfunctioning",
            "I need maintenance on my machine"
        ]
    },
    "Payments": {
        "transcript_index": 0,
        "nav_value": "3",
        "synonyms": [
            "I want to make a payment",
            "I need to pay my bill",
            "I want to pay for my order",
            "I need to settle my invoice",
            "I want to pay online",
            "I need to make a payment",
            "I want to pay my dues",
            "I need to clear my balance",
            "I want to pay for services",
            "I need to handle payment"
        ]
    },
    # TechSupport Inc.
    "Software Issues": {
        "transcript_index": 1,
        "nav_value": "1",
        "synonyms": [
            "I have a software problem",
            "My software is not working",
            "I need help with software",
            "I have a bug in the software",
            "My application is crashing",
            "I need tech support for software",
            "I have an issue with the program",
            "My software is broken",
            "I need help installing software",
            "I have a software error"
        ]
    },
    "Hardware Repair": {
        "transcript_index": 1,
        "nav_value": "2",
        "synonyms": [
            "My computer is broken",
            "I need hardware repair",
            "My device is not working",
            "I have a hardware issue",
            "My laptop needs fixing",
            "I need help with hardware",
            "My device is malfunctioning",
            "I need repair on my equipment",
            "My hardware is broken",
            "I need technical support for hardware"
        ]
    },
    "Account Management": {
        "transcript_index": 1,
        "nav_value": "3",
        "synonyms": [
            "I need to update my account",
            "I want to change my password",
            "I need help with my account",
            "I want to manage my account",
            "I need to update my profile",
            "I have an account issue",
            "I need to reset my password",
            "I want to check my account details",
            "I need to modify my account settings",
            "I have a problem with my login"
        ]
    },
    # BankCorp
    "Checking Accounts": {
        "transcript_index": 2,
        "nav_value": "1",
        "synonyms": [
            "I have a question about my checking account",
            "I need help with my checking account",
            "I want to check my checking balance",
            "I have an issue with my checking account",
            "I need to deposit money into checking",
            "I want to withdraw from checking",
            "I have a problem with my checking account",
            "I need to transfer money from checking",
            "I want to view my checking transactions",
            "I need to order checks"
        ]
    },
    "Savings Accounts": {
        "transcript_index": 2,
        "nav_value": "2",
        "synonyms": [
            "I have a question about my savings account",
            "I need help with my savings account",
            "I want to check my savings balance",
            "I have an issue with my savings account",
            "I need to deposit money into savings",
            "I want to withdraw from savings",
            "I have a problem with my savings account",
            "I need to transfer money from savings",
            "I want to view my savings transactions",
            "I need to open a savings account"
        ]
    },
    "Loans": {
        "transcript_index": 2,
        "nav_value": "3",
        "synonyms": [
            "I want to apply for a loan",
            "I have a question about my loan",
            "I need help with loan payments",
            "I want to check my loan balance",
            "I have an issue with my loan",
            "I need to refinance my loan",
            "I want to pay off my loan early",
            "I have a problem with my loan account",
            "I need to discuss loan options",
            "I want to get a loan statement"
        ]
    },
    "Credit Cards": {
        "transcript_index": 2,
        "nav_value": "4",
        "synonyms": [
            "I have a question about my credit card",
            "I need help with my credit card",
            "I want to check my credit card balance",
            "I have an issue with my credit card",
            "I need to make a credit card payment",
            "I want to report a lost credit card",
            "I have a problem with my credit card",
            "I need to dispute a charge",
            "I want to increase my credit limit",
            "I need to activate a new credit card"
        ]
    },
    # TravelCo
    "Flight Bookings": {
        "transcript_index": 3,
        "nav_value": "1",
        "synonyms": [
            "I want to book a flight",
            "I need help with flight reservations",
            "I want to book a plane ticket",
            "I have an issue with my flight booking",
            "I need to change my flight",
            "I want to cancel a flight",
            "I have a problem with my flight reservation",
            "I need to check flight availability",
            "I want to upgrade my flight",
            "I need to get a boarding pass"
        ]
    },
    "Hotel Reservations": {
        "transcript_index": 3,
        "nav_value": "2",
        "synonyms": [
            "I want to book a hotel",
            "I need help with hotel reservations",
            "I want to reserve a room",
            "I have an issue with my hotel booking",
            "I need to change my hotel reservation",
            "I want to cancel a hotel booking",
            "I have a problem with my hotel reservation",
            "I need to check hotel availability",
            "I want to upgrade my hotel room",
            "I need to get a hotel confirmation"
        ]
    },
    "Car Rentals": {
        "transcript_index": 3,
        "nav_value": "3",
        "synonyms": [
            "I want to rent a car",
            "I need help with car rental",
            "I want to reserve a vehicle",
            "I have an issue with my car rental",
            "I need to change my car reservation",
            "I want to cancel a car rental",
            "I have a problem with my car reservation",
            "I need to check car availability",
            "I want to upgrade my rental car",
            "I need to get a rental confirmation"
        ]
    },
    "Cancellations": {
        "transcript_index": 3,
        "nav_value": "4",
        "synonyms": [
            "I want to cancel my booking",
            "I need to cancel a reservation",
            "I want to cancel my flight",
            "I have an issue with cancellation",
            "I need to cancel my hotel",
            "I want to cancel my car rental",
            "I have a problem with cancelling",
            "I need to get a refund",
            "I want to cancel my trip",
            "I need to speak to cancellations"
        ]
    },
    # HealthPlus
    "Appointments": {
        "transcript_index": 4,
        "nav_value": "1",
        "synonyms": [
            "I want to schedule an appointment",
            "I need help with appointment scheduling",
            "I want to book a doctor's visit",
            "I have an issue with my appointment",
            "I need to reschedule an appointment",
            "I want to cancel an appointment",
            "I have a problem with my appointment",
            "I need to check appointment availability",
            "I want to confirm my appointment",
            "I need to speak to appointments"
        ]
    },
    "Prescription Refills": {
        "transcript_index": 4,
        "nav_value": "2",
        "synonyms": [
            "I need to refill my prescription",
            "I want to get my medication refilled",
            "I have an issue with prescription refill",
            "I need to order my medicine",
            "I want to renew my prescription",
            "I have a problem with my medication",
            "I need to get a refill",
            "I want to check prescription status",
            "I need to talk to pharmacy",
            "I need help with refills"
        ]
    },
    "Billing Inquiries": {
        "transcript_index": 4,
        "nav_value": "3",
        "synonyms": [
            "I have a question about my bill",
            "I need help with medical billing",
            "I want to understand my charges",
            "I have an issue with my bill",
            "I need to dispute a charge",
            "I want to set up a payment plan",
            "I have a problem with my bill",
            "I need to check my balance",
            "I want to get a copy of my bill",
            "I need to speak to billing"
        ]
    },
    "Emergency Services": {
        "transcript_index": 4,
        "nav_value": "4",
        "synonyms": [
            "I have a medical emergency",
            "I need emergency assistance",
            "I need to speak to emergency services",
            "I have an urgent medical issue",
            "I need immediate help",
            "I have a health emergency",
            "I need to call an ambulance",
            "I have a life-threatening situation",
            "I need emergency medical help",
            "I need to get to the emergency room"
        ]
    }
}

def generate_dataset(num_samples: int = 100) -> List[Dict[str, Any]]:
    """Generate synthetic dataset for IVR navigation."""
    dataset = []

    # Flatten the intent mapping to get all possible intents with their details
    all_intents = []
    for intent_name, details in INTENT_MAPPING.items():
        all_intents.append({
            "intent_name": intent_name,
            "transcript_index": details["transcript_index"],
            "nav_value": details["nav_value"],
            "synonyms": details["synonyms"]
        })

    # Generate samples
    for _ in range(num_samples):
        # Randomly select an intent
        intent_data = random.choice(all_intents)

        # Randomly select a synonym for the intent
        user_intent = random.choice(intent_data["synonyms"])

        # Get the transcript
        transcript = IVR_TRANSCRIPTS[intent_data["transcript_index"]]

        # Create the navigation command
        nav_command = {
            "navType": "Press",
            "navValue": intent_data["nav_value"]
        }

        # Create the conversation in OpenAI chat format
        conversation = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are an IVR navigation assistant."
                },
                {
                    "role": "user",
                    "content": f"Transcript: {transcript} User Intent: {user_intent}"
                },
                {
                    "role": "assistant",
                    "content": json.dumps({"series_of_commands": [nav_command]})
                }
            ]
        }

        dataset.append(conversation)

    return dataset

def split_dataset(dataset: List[Dict[str, Any]], train_ratio: float = 0.7, val_ratio: float = 0.15) -> tuple:
    """Split dataset into train, validation, and test sets."""
    random.shuffle(dataset)
    total = len(dataset)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)

    train_data = dataset[:train_end]
    val_data = dataset[train_end:val_end]
    test_data = dataset[val_end:]

    return train_data, val_data, test_data

def save_jsonl(data: List[Dict[str, Any]], file_path: str):
    """Save data in JSONL format."""
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

def main():
    # Generate dataset
    print("Generating synthetic dataset...")
    dataset = generate_dataset(100)

    # Split dataset
    train_data, val_data, test_data = split_dataset(dataset)

    # Save datasets
    save_jsonl(train_data, "data/train.jsonl")
    save_jsonl(val_data, "data/validation.jsonl")
    save_jsonl(test_data, "data/test.jsonl")

    print(f"Generated {len(train_data)} training samples")
    print(f"Generated {len(val_data)} validation samples")
    print(f"Generated {len(test_data)} test samples")
    print("Dataset saved to data/")

if __name__ == "__main__":
    main()