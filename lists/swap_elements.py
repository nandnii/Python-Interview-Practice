def swap(lst, i, j):
    if len(lst) < 2:
        # Nothing to interchange
        return lst

    # Swap first and last
    lst[i], lst[j] = lst[j], lst[i]
    return lst


if __name__ == "__main__":
    # Input: space-separated integers
    arr = list(map(int, input("Enter list elements separated by space: ").split()))
    idx1 = int(input("Enter first index: "))
    idx2 = int(input("Enter second second: "))
    
    result = swap(arr, idx1, idx2)
    print("List after interchange:", result)
