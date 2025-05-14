import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    print(f"Think of a number between {low} and {high}. I (the computer) will try to guess it!")

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high, doesn't matter here

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number, {guess}, correctly! 🎉")
        else:
            print("Please enter H (high), L (low), or C (correct).")

# Run the game
computer_guess(100)
