def ispalindrome(a):
    
    a = a.lower()

    if a == a[::-1]:
        return "The AplhaNumeric Word is Palindrome"
    else:
        return "The AplhaNumeric Word is Not Palindrome" 


a = input("Enter an AplhaNumeric Word: ")

print(ispalindrome(a))

