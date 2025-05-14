import random

def main(): 
    for i in range(10):
        number = random.randint(1, 100)
        print(number, end=" ")

if __name__ == "__main__":
    main()