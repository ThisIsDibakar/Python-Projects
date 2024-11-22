print("\n")

with open ('02 PROJECTS/07 Currency Converter/CurrencyData.txt') as f:
	lines = f.readlines()

currencyDict = {}
for line in lines:
	parsed = line.split("\t")
	currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount in INR : "))

print("\n")

print("Enter the name of the Currency to convert this amount\nAvailable Options:\n")
[print(item) for item in currencyDict.keys()]

print("\n")

currency = input("Please enter one of these values: ")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")

print("\n")