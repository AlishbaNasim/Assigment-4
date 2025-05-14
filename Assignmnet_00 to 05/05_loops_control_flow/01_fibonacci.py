
def main():

    # Constant for the maximum value
    MAX_VALUE = 10000

    # First two terms of Fibonacci sequence
    a, b = 0, 1

    # Print terms while less than MAX_VALUE
    while a < MAX_VALUE:
        print(a, end=' ')
        a, b = b, a + b

if __name__ == '__main__':
    main()
