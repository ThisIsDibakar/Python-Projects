def main():

    prices = []

    Sum = 0
    Y = 1

    while True:

        try:

            print("\n")

            B = int(input("Enter Price to add or 0 to Quit: \n"))
            prices.append(B)

            if B == 0:
                print("\n")
                prices.pop(-1)
                print(f"Your total Bill is Rs {Sum}")
                print("\n")
                print("Your Bill Summary is: ")
                for item in prices:
                    print(Y, "\b]", "Rs", item)
                    Y = Y + 1
                print("\n")
                print("Thank You for Shopping")
                break

            Sum = Sum + B

            print("\n")

            print(Sum)


        except ValueError:
            
            print("\n")
            print("INPUT IS NOT AN INTEGER")
            print("Please Try Again")
            print("\n")



if __name__ == '__main__':
    main()


print("\n")