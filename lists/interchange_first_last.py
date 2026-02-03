def interchange_first_last(lst):
    if len(lst) < 2:
        # Nothing to interchange
        return lst

    # Swap first and last
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


if __name__ == "__main__":
    # Input: space-separated integers
    arr = list(map(int, input("Enter list elements separated by space: ").split()))
    
    result = interchange_first_last(arr)
    print("List after interchange:", result)
