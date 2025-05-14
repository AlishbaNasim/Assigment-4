def get_first_element(lst):
    # List ka pehla element print karo
      print(lst[0])

def main():
    # List ko user se input karwana (one element at a time)
    lst = []
    n = int(input("Enter the number of elements in the list: "))
    
    for i in range(n):
        element = input(f"Enter element {i + 1}: ") #iteration hoga.
        lst.append(element)
    
    # First element print karne wali function call karo
    get_first_element(lst)

if __name__ == "__main__":
    main()
