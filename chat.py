import re
import random
import datetime

# Define intent patterns using regular expressions
patterns = {
    "greeting": re.compile(r"\b(hello|hi|hey)\b", re.IGNORECASE),
    "farewell": re.compile(r"\b(bye|goodbye|see you)\b", re.IGNORECASE),
    "time": re.compile(r"what.*time", re.IGNORECASE),
    "date": re.compile(r"what.*date", re.IGNORECASE),
    "target": re.compile(r"target.*week", re.IGNORECASE),
    "achievements": re.compile(r"achievements", re.IGNORECASE),
    "future_plans": re.compile(r"future.*work.*plans", re.IGNORECASE),
}

# Helper functions for dynamic responses
def get_time():
    """Returns the current time in a human-readable format (e.g., 02:30 PM)."""
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    """Returns the current date in a human-readable format (e.g., June 22, 2025)."""
    return datetime.datetime.now().strftime("%B %d, %Y")

# Define responses as lambda functions for flexibility
responses = {
    "greeting": lambda: random.choice(["Hello!", "Hi there!", "Hey!"]),
    "farewell": lambda: random.choice(["Goodbye!", "See you later!", "Bye!"]),
    "time": lambda: f"The current time is {get_time()}.",
    "date": lambda: f"Today's date is {get_date()}.",
    "target": lambda: "The target for this week is to complete the chatbot project.",
    "achievements": lambda: "So far, I have implemented the basic structure of the chatbot.",
    "future_plans": lambda: "In the future, I plan to add more intents and improve the natural language understanding.",
    "default": lambda: random.choice([
        "I'm sorry, I didn't understand that.",
        "Can you please rephrase?",
        "I don't know how to respond to that."
    ])
}

# Function to match user input to an intent
def match_intent(user_input):
    """
    Matches the user's input to a predefined pattern.
    Returns the intent name if matched, otherwise 'default'.
    """
    for intent, pattern in patterns.items():
        if pattern.search(user_input):
            return intent
    return "default"

# Function to generate a response based on the intent
def generate_response(intent):
    """Generates a response by calling the corresponding lambda function."""
    return responses[intent]()

# Main chatbot loop
print("Welcome to the chatbot! Type 'quit' to exit.")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    intent = match_intent(user_input)
    response = generate_response(intent)
    print("Chatbot:", response)