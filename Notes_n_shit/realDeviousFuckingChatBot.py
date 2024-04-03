#CHATBOT
#https://github.com/FreeBirdsCrew/AI_ChatBot_Python
#https://github.com/Elysian01/AI-Chatbot

import regex

def get_task_name(user_input):
    # You could use more advanced parsing or NLP here
    return user_input.split("name is ")[1] if "name is " in user_input else "Unknown Task"

# Assume we're adding more functions to handle each step of scheduling

def chatbot():
    print("Hello! I'm your scheduling assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        if "schedule" in user_input.lower():
            print("Bot: What is the task name?")
            task_name = get_task_name(input("You: "))
            # Continue asking for more info (date, participants, etc.)
            print(f"Bot: Got it. I'll schedule '{task_name}' for you.")
        elif "help" in user_input.lower():
            print("Bot: I can help schedule tasks. Try saying 'schedule a meeting'.")
        elif "quit" in user_input.lower():
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I'm not sure how to help with that.")

if __name__ == "__main__":
    chatbot()
