import random

NUM_SIDES: int = 6

def main():

    # die rolling
    die1: int = random.randint(1 , NUM_SIDES)
    die2: int = random.randint(1 , NUM_SIDES)
    
    # SUM OF 2 DIE
    total: int = die1 + die2

    # print all thing

    print(f"DIE HAVE {NUM_SIDES} SIDES EACH.")
    die1: int = random.randint(1 , NUM_SIDES)
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice : {total}")


if __name__ == '__main__':
    main()