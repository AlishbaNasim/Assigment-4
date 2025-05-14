import random
import string

# List of possible words
words = ['python', 'hangman', 'challenge', 'keyboard', 'awesome']

# Function to get a valid word
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the user has guessed

    lives = 6

    print("Welcome to Hangman! 🎯")

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left. You've used these letters: {' '.join(used_letters)}")

        # Current state of the word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You already used that letter.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"\nYou died, sorry. The word was {word}")
    else:
        print(f"\n🎉 You guessed the word: {word}!")

# Run the game
hangman()
