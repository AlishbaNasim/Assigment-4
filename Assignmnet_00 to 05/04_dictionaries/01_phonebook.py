def main():
    phonebook = {}

    while True:
        name = input("Enter a name (or press Enter to stop): ")
        if name == "":
            break

        number = input(f"Enter the phone number for {name}: ")
        phonebook[name] = number

    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

if __name__ == "__main__":
    main()
