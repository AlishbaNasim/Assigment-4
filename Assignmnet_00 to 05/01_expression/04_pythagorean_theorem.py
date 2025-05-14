import math

def main():
    print("Let's find the hypotenuse of a right triangle!")

    side1: float = float(input( "Enter the length of AB: " ))
    side2: float = float(input( "Enter the length of AC: " ))

    hypotenuse: float = math.sqrt( side1 ** 2 + side2 ** 2 )
    print(f"The Length of hypotenuse (BC) is: {hypotenuse} ")

if __name__ == '__main__':
    main()