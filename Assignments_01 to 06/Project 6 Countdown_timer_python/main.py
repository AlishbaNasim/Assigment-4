import time
# time.sleep() to delay execution

# divmod() for formatting MM:SS

# while loop for countdown

# Input handling and basic validation

# end="\r" to overwrite the same line in terminal

# Function to run the countdown
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert to MM:SS format
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Print in place
        time.sleep(1)
        seconds -= 1

    print("Time's up! ⏰")

# Ask the user for input
user_input = input("Enter the time in seconds: ")

# Check if input is a valid number
if user_input.isdigit():
    countdown_timer(int(user_input))
else:
    print("Please enter a valid number.")
