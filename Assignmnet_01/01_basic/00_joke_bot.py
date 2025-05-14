def joke_bot():
    print("Hi! I'm JokeBot. What would you like?")
    user_input = input("Type your request: ")

    if user_input == "Joke":
        print("Why don't programmers like nature? It has too many bugs! 🐛")
    else:
        print("Sorry, I only tell jokes. Try typing 'Joke'.")

joke_bot()
