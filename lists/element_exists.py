def exist(lst, num):
    return num in lst


if __name__ == "__main__":
    # Input: space-separated integers
    arr = list(map(int, input("Enter list elements separated by space: ").split()))
    num = int(input("Enter number to check: "))
    
    result = exist(arr, num)
    print("Does this number exist?:", result)
