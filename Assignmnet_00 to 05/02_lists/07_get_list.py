def main():
    my_list = []

    while True:
        value = input("Enter a value (or press Enter to finish): ")
        
        if value == "":
            break  # Exit the loop if input is empty
        
        my_list.append(value)  # Add the value to the list

    print("Your list is:", my_list)

if __name__ == "__main__":
    main()
