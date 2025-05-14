def main():
    Inches: int = 12  # type hint with assignment
    feet: float = float(input("Enter your feet? "))
    feet_into_inches: float = feet * Inches
    print(f"This is {feet_into_inches} inches!")

if __name__ == '__main__':
    main()