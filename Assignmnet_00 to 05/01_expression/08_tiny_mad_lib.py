SENTENCE_START: str = "In my coding journey, I built a very "


def main():
    print("Welcome to the Mad Lib Game! 🤩")
    print("Please answer the following questions:")
    # Get the three inputs from the user to make the Madlib
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")



if __name__ == '__main__':
    main()