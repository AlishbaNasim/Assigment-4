import random

def main():
    # Step 1: Computer picks a random number between 0 and 99
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    # Step 2: Keep asking user for guesses until they get it right
    while True:
        guess = int(input("Enter a guess: "))
        
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break

if __name__ == '__main__':
    main()