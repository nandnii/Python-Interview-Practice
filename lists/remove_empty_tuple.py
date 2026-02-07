def remove(arr):

    # By set we'll do this in O(1)
    return [x for x in arr if x != ()]

if __name__ == "__main__":
    # Input: space-separated integers
    arr = [(1,2), (), (5,), 6]
    
    result = remove(arr)
    print("List after removal:", result)
