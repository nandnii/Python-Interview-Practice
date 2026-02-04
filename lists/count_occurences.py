def count(lst, num):
    
    # # Using built in func
    # return lst.count(num)

    # Using loop
    counter = 0
    for i in lst:
        if i == num:
            counter += 1

    return counter



if __name__ == "__main__":
    # Input: space-separated integers
    arr = list(map(int, input("Enter list elements separated by space: ").split()))
    num = int(input("Enter number to count: "))
    
    result = count(arr, num)
    print(f"{num} exists {result} times")
