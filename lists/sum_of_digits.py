def sum(lst):
    new = []

    # # Using string manipulation
    # for num in lst:
    #     num_sum = 0
        
    #     for x in str(abs(num)): # handle negative nums by doing abs
    #         num_sum += int(x)
        
    #     # print(num_sum) # Print sum of digit of all elements
        
    #     new.append(num_sum)
        
    # return new

    # Without string manipulation
    for val in lst:
        total = 0
        while val > 0:
            total += val % 10   # Used to get last digit
            val //= 10          # Used to remove last digit
        new.append(total)

    return new


if __name__ == "__main__":
    # Input: space-separated integers
    arr = list(map(int, input("Enter list elements separated by space: ").split()))
    
    result = sum(arr)
    print("List with sum of digits for each element:", result)
