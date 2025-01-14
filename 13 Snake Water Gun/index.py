import random

print("\n")
print("Welcome To Snake Water Gun")
print("\n")


def checkAnswer(user_choice, comp_choice):
    if user_choice == comp_choice:
        print("DRAW !!!")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
        print("YOU LOSE !!!")
    else:
        print("YOU WIN !!!")


def userAnswer(user_choice):
    if user_choice == 0:
        print("You chose SNAKE or ROCK")
    elif user_choice == 1:
        print("You chose WATER or SCISSORS")
    else:
        print("You chose GUN or PAPER")


def machineAnswer(comp_choice):
    if comp_choice == 0:
        print("Computer chose SNAKE or ROCK")
    elif comp_choice == 1:
        print("Computer chose WATER or SCISSORS")
    else:
        print("Computer chose GUN or PAPER")


while True:

    print("ENTER 0 for SNAKE or ROCK")
    print("ENTER 1 for WATER or SCISSORS")
    print("ENTER 2 for GUN or PAPER")
    print("\n")
    print("ENTER 5 to QUIT :)")

    print("\n")

    try:
        user_choice = int(input("Enter Your Choice:\n"))
        comp_choice = random.randint(0, 2)
        print("\n")

        if user_choice in [0, 1, 2]:
            userAnswer(user_choice)
            machineAnswer(comp_choice)
            checkAnswer(user_choice, comp_choice)
            print("\n")
        elif user_choice == 5:
            print("Thank You for Playing")
            break
        else:
            print("Not a VALID Integer")
            print("\n")

    except ValueError:
        print("Character entered is not an INTEGER")
        print("Please Try Again")
        print("\n")

print("\n")
