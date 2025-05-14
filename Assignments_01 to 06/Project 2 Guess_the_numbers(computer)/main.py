import random

def guess_the_number():
    print("🎮 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100...")

    secret_number = random.randint(1, 100)
    guess = None # guess is used to store the user's input.
    attempts = 0 # attempts keeps track of how many guesses the user makes.

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} tries. The number was: {secret_number}")
        except ValueError:
            print("❌ Please enter a valid number.")

# Run the game
guess_the_number()
