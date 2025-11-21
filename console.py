from model import UTPAssistModel

def main():
    print("Welcome to UTP Resident Assist Bot!")
    
    try:
        bot = UTPAssistModel()
        print("Chatbot model loaded successfully.\n")
    except FileNotFoundError as e:
        print("ERROR:", e)
        return

    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        
        response = bot.get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
