import random
import string

print("\n")


def RandomFixLenAlphaString():
    CH = ""
    i = 0
    while i < 3:
        CH += random.choice(string.ascii_letters)
        i += 1
    return CH


def EnCode():
    nWords = []
    for word in words:
        if (len(word) >= 3):
            newString = RandomFixLenAlphaString(
            ) + word[1:] + word[0] + RandomFixLenAlphaString()
            nWords.append(newString)
        else:
            nWords.append(word[::-1])
    print("EnCoded Message :")
    print(" ".join(nWords))


def DeCode():
    nWords = []
    for word in words:
        if (len(word) >= 3):
            newString = word[3:-3]
            newString = newString[-1] + newString[:-1]
            nWords.append(newString)
        else:
            nWords.append(word[::-1])
    print(" ".join(nWords))


print("Enter 1 to EnCode")
print("Enter 0 to DeCode")
print("\n")
ch = int(input("Enter Your Choice: "))
print("\n")


st = input("Enter Message:\n")
words = st.split(" ")


print("\n")
print("Message:")
print(words)
print("\n")


EnCode() if (ch == 1) else DeCode() if (ch == 0) else print("INVALID INPUT")


print("\n")
