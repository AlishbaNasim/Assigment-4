# Mad Libs Python Project

# Prompting the user to enter words
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
celebrity = input("Enter a celebrity's name: ")
animal = input("Enter an animal: ")

# Generating the story
story = f"Once upon a time, in a {place} far, far away, there was a {adjective} {noun} who loved to {verb}. Every day, it would {verb} in the fields, and one day, it met a {animal}. The {animal} told the {noun} that it had just seen {celebrity} walking by. The {noun} was so excited that it started to {verb} even more."

# Output the Mad Libs story
print("\nHere is your Mad Libs story:")
print(story)
