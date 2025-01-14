print("\n")

print("Welcome To Calculator")

while True:

    print("\n")

    A = int(input("Enter First Number: "))
    B = int(input("Enter Second Number: "))

    print("\n")

    print("Enter 1 to Perform ADDITION")
    print("Enter 2 to Perform SUBTRACTION")
    print("Enter 3 to Perform MULTIPLICATION")
    print("Enter 4 to Perform DIVISION")
    print("Enter 5 to Perform FLOOR DIVISION")
    print("Enter 6 to Perform MODULUS")
    print("Enter 7 to Perform EXPONENT")

    print("\n")

    X = int(input("Enter Your Choice : "))

    if X == 1:
        print("\nThe Answer is:", A+B)
    elif X == 2:
        print("\nThe Answer is:", A-B)
    elif X == 3:
        print("\nThe Answer is:", A*B)
    elif X == 4:
        print("\nThe Answer is:", A/B)
    elif X == 5:
        print("\nThe Answer is:", A//B)
    elif X == 6:
        print("\nThe Answer is:", A % B)
    elif X == 7:
        print("\nThe Answer is:", A**B)
    else:
        print("ERROR: INVALID INPUT")

    print("\n")

    print("Enter Y to PERFORM AGAIN")
    print("Enter N to QUIT")

    print("\n")

    Y = input("Enter Your Choice: ")

    print("\n")

    if Y == "Y" or Y == "y":
        pass
    elif Y == "N" or Y == "n":
        break
    else:
        print("ERROR: INVALID INPUT!")
        print("~ BREAKING PROGRAM")
        print("\n")
        break


print("Thank You")

print("\n")
