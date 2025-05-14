def get_last_element(last):
    # List ka pehla element print karo
      print(last[-1])

def main():
    # List ko user se input karwana (one element at a time)
    last = []
    n = int(input("Enter the number of elements in the list: "))
    
    for i in range(n):
        element = input(f"Enter element {i + 1}: ") #iteration hoga.
        last.append(element)
    
    # last element print karne wali function call karo
    get_last_element(last)

if __name__ == "__main__":
    main()
