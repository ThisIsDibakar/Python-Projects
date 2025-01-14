print("\n")


def Factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * Factorial(n - 1)


if __name__ == "__main__":
    x = int(input("Enter the Number whose Factorial is to be Calculated:\n"))
    print("\n")
    print("The Factorial of", x, "is:", Factorial(x))


print("\n")
