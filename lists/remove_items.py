def remove(arr, rem):

    # By set we'll do this in O(1)
    rem_set = set(rem)

    return [x for x in arr if x not in rem_set]


if __name__ == "__main__":
    # Input: space-separated integers
    arr = list(map(int, input("Enter list elements separated by space: ").split()))

    rem = list(map(int, input("Enter list elements to be removed separated by space: ").split()))
    
    result = remove(arr, rem)
    print("List after removal:", result)
