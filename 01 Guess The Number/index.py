import random

print("\nWelcome to the Number Guessing Game!\n")
attempts = 0

while True:
    a = random.randint(1, 10)  # Random number between 1 and 10
    print("Enter a Number between 1 to 10: ")
    print("Or Enter 0 to Quit: ")
    b = int(input("Input: "))

    if b == 0:  # Quit condition
        print("Thank You for Playing!")
        break

    if 1 <= b <= 10:  # Valid input range
        attempts += 1
        if a == b:
            print(f"The Number was Indeed {a}")
            print("Correct Guess!!! \n")
            print(f"Congratulations, You guessed the Correct Number in {
                  attempts} attempts")
            break  # End the game after correct guess
        else:
            print(f"The Number was {a}")
            print("Wrong Guess, Try Again! \n")
    else:
        print("Please Enter a Number within the Range 1 to 10 \n")
