import random

print("\n")

print("Welcome to HangMan :)")

print("\n")

print("Rules: ")
print("Guess the Characters of a Random Word")
print("Attempts: 07")

print("\n")

while True:

    print("\n")

    words = [ 'apple', 'banana', 'chocolate', 'elephant', 'furniture', 'giraffe', 'hamburger', 'internet', 'jacket', 'kangaroo', 'leopard', 'mountain', 'notebook', 'ostrich', 'pineapple', 'question', 'rainbow', 'strawberry', 'telephone', 'umbrella', 'violin', 'watermelon', 'xylophone', 'yellow', 'zebra', 'aardvark', 'butterfly', 'catapult', 'dinosaur', 'elephant', 'flamingo', 'gorilla', 'hedgehog', 'iguana', 'jellyfish', 'koala', 'lighthouse', 'mongoose', 'narwhal', 'octopus', 'penguin', 'quokka', 'rhinoceros', 'salamander', 'toucan', 'unicorn', 'vulture', 'walrus', 'xray', 'yak', 'zeppelin', 'acrobat', 'ballet', 'circus', 'dancer', 'elephant', 'fireworks', 'gymnastics', 'hula hoop', 'skating', 'juggler', 'karate', 'lion tamer', 'magician', 'unicycle', 'ventriloquist', 'whirligig', 'xylophone', 'yoyo', 'zookeeper', 'astronomy', 'biology', 'chemistry', 'dinosaur', 'ecology', 'forensics', 'geology', 'history', 'insect', 'journalism', 'kinesiology', 'linguistics', 'meteorology', 'nautical', 'oceanography', 'paleontology', 'quantum', 'robotics', 'sociology', 'technology', 'uranium', 'volcano', 'weather', 'xenophobia', 'yacht', 'zoology', 'algorithm', 'binary', 'computer', 'database', 'encryption', 'firewall', 'programming', 'software', 'telecommunication', 'virtual', 'wireless', 'xylophone', 'youtube', 'zipper', 'abundance', 'benevolent', 'courageous', 'determined', 'enthusiasm', 'fascinating', 'gratitude', 'happiness', 'imagination', 'jubilant', 'kindness', 'luminous', 'magnificent', 'nurturing', 'optimistic', 'passionate', 'quizzical', 'resilient', 'serendipity', 'tranquility', 'unwavering', 'vibrant', 'wonderful', 'xenodochial', 'yearning', 'zealous' ]

    words_try = [ 'Furniture', 'Happiness', 'Classify', 'telecommunication' ]

    SplitWord = {}
    Answer = {}
    
    dict_1 = {}
    dict_2 = {}

    Guesses = 1
    AttemptsR = 7

    word = random.choice(words)
    word = word.lower()

    for letters in range(len(word)):
        SplitWord[letters] = word[letters]
        dict_1[letters + 1] = word[letters]
        dict_2[letters + 1] = "_"

    print("The Word is a", len(word), "Character Word \n")

    while True:

        char = input((f"Guess {Guesses} : "))
        print("\n")

        View = []

        y = 0

        if char in SplitWord.values():
            print("Correct Guess!!")

            for i in range(1, len(word)+1):

                y = y + 1

                if char == word[i-1]:
                    View.append(y)
                    # Answer.update({i - 1 , SplitWord[i-1]})                       # Update Method Not Working, Why??
                    Answer[i-1] = SplitWord[i-1]                                    # Used Raw Method of dict, Successfully Working...
                    
                    if not dict_2[i] == dict_1[i]:
                        dict_2.update({i : char})

            print(char, "is Present at Position(s)", View, "\n")
            # print(dict_1)
            print("\nProgress:", list(dict_2.values()), "\n")
            # print("\nProgress:", list(dict_2.values()), "\n")

            if Answer == SplitWord:
                print("Congratulations, The Word was:", word.upper(), "\n")
                print("The Man was saved from being Hanged!!!")
                break

        else:
            print("Incorrect Guess")
            AttemptsR = AttemptsR - 1
            print(f"Attempts Remaining:", {AttemptsR}, "\n")
            print("\nProgress:", list(dict_2.values()), "\n")

        if AttemptsR == 0:
            print("Game Lost \n")
            print("The Word was:", word.upper())
            break

        Guesses = Guesses + 1

    print("\n")
    C = input("Enter Y to Play Again or N to Quit: ")

    if not C.lower() == "y":
        print("\n")
        print("Thank You for Playing, Adios \n")
        break

print("\n")
