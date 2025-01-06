# **AI Chatbot with NLP**

**Name:** Soham Dutta  
**Company:** CODTECH IT Solutions  
**ID:** CT08EIL  
**Domain:** Python Programming  

---

## **Objective**  
Develop an interactive chatbot capable of responding to user queries intelligently, providing assistance with greetings, farewells, and basic help-related topics. The chatbot uses NLP to understand and classify user input.

---

## **Key Features**

1. **Natural Language Processing (NLP):**  
   - Utilizes **SpaCy's English language model (`en_core_web_sm`)** for tokenization and intent classification.

2. **Intent Classification:**  
   - Detects user intent based on keywords and lemmatized tokens in the input.  
   - Supported intents include:  
     - **Greeting:** Recognizes "hello," "hi," or similar expressions.  
     - **Farewell:** Identifies phrases like "bye" or "goodbye."  
     - **Name Inquiry:** Responds when the chatbot's name is mentioned.  
     - **Help Request:** Detects keywords like "help" or "assist."  
     - **Default:** Handles unrecognized input with fallback responses.

3. **Dynamic Responses:**  
   - Provides varied replies using a randomized selection from predefined responses for each intent.  

4. **User Interaction:**  
   - Accepts user input via the command line and generates conversational responses in real-time.  
   - Offers a smooth exit option when the user types "exit."

---

## **Technologies Used**

- **Python Modules:**  
  - **`spacy`**: Implements NLP capabilities for input analysis and intent classification.  
  - **`random`**: Randomizes responses for a natural conversational experience.

- **NLP Model:**  
  - **SpaCy's `en_core_web_sm`**: Processes and analyzes English text for tokenization, lemmatization, and intent detection.

---

## **Outcome**

The Codtech AI Chatbot provides an interactive, user-friendly experience with capabilities for basic conversational understanding. It demonstrates fundamental natural language processing techniques and serves as a foundational chatbot application.

---

## **Sample Interaction**

### **Scenario 1: Greeting**
- **User:** Hello  
- **Chatbot:** Hi there! How may I help you?

### **Scenario 2: Name Inquiry**
- **User:** What is your name?  
- **Chatbot:** I'm Codtech Assistant, your chatbot! I'm built by Soham Dutta.

### **Scenario 3: Exit**
- **User:** Exit  
- **Chatbot:** Goodbye!

---

## **Screenshot**

![ai-chatbot](https://github.com/user-attachments/assets/6eb0b9d5-292d-49a9-a71c-9e32604bcc98)
