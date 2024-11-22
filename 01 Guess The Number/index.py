import random

print("\n")

attempts = 0

while True:

    a = random.randint(1, 10)

    print("Enter a Number between 1 to 10: ")
    print("Or Enter 0 to Quit: ")
    b = int(input("Input: "))

    if a >= 0 and a <= 10:

        if a == b:
            print("The Number was Indeed", a)
            print("Correct Guess !!! \n")
            print(f"Congratulation, You gussed the Correct Number in {
                  attempts} attempts")
        elif a == 0:
            print("Thank You for Playing")
            break
        else:
            print("The Number was", a)
            print("Wrong Guess, Try Again \n")
    else:
        print("Enter a Number within Range \n")

    attempts += 1

print("\n")
