
def main():
    counts = {}

    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        number = int(number)
        
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    for number, count in counts.items():
        print(f"{number} appears {count} times.")


if __name__ == "__main__":
    main()
