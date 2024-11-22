print("\n")

MorseDict = { 
	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
	}

K = list(MorseDict.keys())
V = list(MorseDict.values())





def EnCode():

	Cipher = []

	print("Enter a ',' (comma) after every Word to help Decode the Morse Code")
	Text = input("Enter Your Message:\n")
	Text = Text.upper()
	TextSplit = Text.split(" ")

	print("\n")
	
	
	for element in TextSplit:
		for letter in element:
			Cipher.append(MorseDict[letter])
			Cipher.append('   ')

		Cipher.append('    ')

	print("EnCoded Message: ")
	print("".join(Cipher))
	print("\n")


def DeCode():
	
	DeCipher = []


	Code = input("Enter Code: ")
	Code = Code.split('       ')
	Code = ("   ".join(Code))
	Code = Code.split('   ')


	print("\n")


	for letters in Code:
		for count, obj in enumerate(V):
			if obj == letters:
				DeCipher.append(K[count])
	DeCipher.append('       ')

	print("For Help, Every Word is Separated by commas (,)\n")
	print("DeCoded Message: ")
	Z = "  ".join(DeCipher)
	print(Z.upper())
	print("\n")


def main():

	print("Enter 1 to EnCode")
	print("Enter 0 to DeCode")
	print("\n")
	ch = int(input("Enter Your Choice: "))
	print("\n")


	# EnCode() if ch == 1 else DeCode() if ch == 0 else print("INVALID INPUT")

	if ch == 1:
		EnCode()
	elif ch == 0:
		DeCode()
	else:
		print("INVALID INPUT")


if __name__ == '__main__':
	main()



print("\n")