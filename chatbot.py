import random
import spacy
from spacy.lang.en import English

# Loading Spacy's English language model
nlp = spacy.load('en_core_web_sm')

# Sample responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! How may I help you?"],
    "farewell": ["Goodbye! Have a great day!", "See you later!"],
    "name": ["I'm Codtech Assistant, your chatbot! I'm built by Soham Dutta"],
    "help": ["I'm here to assist with your questions. Try asking me about our services or internship details."],
    "default": ["I'm sorry, I didn't understand that. Could you rephrase it?", "Could you please clarify your query?"]
}

# Function to classify user input
def classify_intent(user_input):
    doc = nlp(user_input.lower())
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greeting"
        elif token.lemma_ in ["bye", "goodbye"]:
            return "farewell"
        elif "name" in user_input.lower():
            return "name"
        elif "help" in user_input.lower() or "assist" in user_input.lower():
            return "help"
    return "default"

# Function to generate a chatbot response
def chatbot_response(user_input):
    intent = classify_intent(user_input)
    return random.choice(responses[intent])

if __name__ == "__main__":
    print("Welcome to Codtech AI Chatbot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")