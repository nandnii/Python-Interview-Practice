def dup(arr):

    set_l = set()
    ans = set()

    for i in arr:
        if i not in set_l:
            set_l.add(i)     # if i coming for first time then set_l
        else:
            ans.add(i)       # if i is coming more than once then ans

    return ans

if __name__ == "__main__":
    # Input: space-separated integers
    arr = list(map(int, input("Enter list elements separated by space: ").split()))
    
    result = dup(arr)
    print("Duplicate items:", result)
