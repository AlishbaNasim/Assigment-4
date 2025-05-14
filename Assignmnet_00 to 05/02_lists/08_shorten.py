MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()       # Last item remove karo
        print(removed)            # Remove kiya hua item print karo


def main():
    lst = []
    num= int(input("Enter number of items: "))
    for i in range(num):
        item = input(f"Enter item {i+1}: ")
        lst.append(item)
    
    shorten(lst)
    print("Final list:", lst)

if __name__ == "__main__":
    main()
