def reverse(lst):
    
    # # Using in place method
    # lst.reverse()
    # return lst

    # # Using slicing
    # return lst[::-1]

    # Using loop
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst



if __name__ == "__main__":
    # Input: space-separated integers
    arr = list(map(int, input("Enter list elements separated by space: ").split()))
    
    result = reverse(arr)
    print("List after reversal:", result)
