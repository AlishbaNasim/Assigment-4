import random 

def roll_dice():
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    print(f"Die 1: {die1} , Die 2: {die2}")

def main():
    print("Rolling two dices,three times....")
    print() # for spacing
    for i in range(3):
        print(f"Roll { i + 1 }:")
        roll_dice()
        print() # for spacing


if __name__ ==  '__main__':
    main()    

