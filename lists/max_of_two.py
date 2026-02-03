def find_max(a, b):
    if a > b:
        return a
    else:
        return b


if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = find_max(x, y)
    print("Maximum is:", result)
