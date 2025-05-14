def main():
    numbers: list[int] = [2,4,6,8,10]  

    for i in range(len(numbers)):  #range is built-in fun that use to generate sequence
        elem_at_index = numbers[i]  
        numbers[i] = elem_at_index * 2 

    print(numbers)  # This should print the doubled list




if __name__ == '__main__':
    main()