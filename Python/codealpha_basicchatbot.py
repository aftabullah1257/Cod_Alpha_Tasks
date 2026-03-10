def simple_chatbot():
    print("Chatbot: Hi! I am a simple bot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm fine, thanks!")
        elif "your name" in user_input:
            print("Chatbot: I'm the CodeAlpha Basic Bot.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I am not sure how to answer that yet.")

simple_chatbot()