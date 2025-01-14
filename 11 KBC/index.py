print("\n")

print("Welcome To KBC")

print("\n")

questions = [
    ["I] Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?",
        "Solicitor General", "Attorney General", "Cabinet Secretary", "Chief Justice", 2],

    ["II] Who, in 1978, became the first person to be born in the continent of Antarctica?",
     "Emilio Palma", "James Weddell", "Nathaniel Palmer", "Charles Wilkes", 1],

    ["III] Which colonial power ended its involvement in India by selling the rights of the Nicobar Islands to the British on October 18, 1868?",
     "Belgium", "Italy", "Denmark", "France", 3],

    ["IV] Who is the first woman to successfully climb K2, the world’s second highest mountain peak?",
     "Junko Tabei", "Wanda Rutkiewicz", "Tamae Watanabe", "Chantal Mauduit", 2],

    ["V] Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the ‘Dastan-e-Ghadar’, a personal account of the 1857 revolt?",
     "Mir Taqi Mir", "Mohammad Ibrahim Zauq", "Zahir Dehlvi", "Abul-Qasim Ferdowsi", 3],

    ["VI] The historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were held at which place in Shimla?",
     "Viceregal Lodge", "Gorton Castle", "Barnes Court", "Cecil Hotel", 3],

    ["VII] Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?",
     "Cathay Cinema Hall", "Fort Canning Park", "National University of Singapore", "National Gallery of Singapore", 1],

    ["VIII] Milinda-Panha is a dialogue between King Menander or Milinda and which Buddhist monk?",
     "Asanga", "Nagasena", "Mahadharmarakshita", "Dharmaraksita", 2],

    ["IX] What was the title of the thesis that Dr. B. R. Ambedkar submitted to the London School of Economics for which he was awarded his doctorate in 1923?",
     "The Want and Means of India", "The Problem of the Rupee", "National Dividend of India", "The Law and Lawyers", 2],

    ["X] Which was the first mountain peak above 8,000 metres in height to be summited by humans?",
     "Annapurna", "Lhotse", "Kanchenjunga", "Makalu", 1],

    ["XI] According to the Padma Purana, which king had to live as a tiger for a hundred years due to a deer's curse?",
     "Kshemadhurti", "Dharmadatta", "Mitadhvaja", "Prabhanjana", 4],

    ["XII] Leena Gade, a person of Indian origin, is the first female race engineer to win which of the following races?",
     "Indianapolis 500", "24 Hours of Le Mans", "12 Hours of Sebring", "Monaco Grand Prix", 2],

    ["XIII] Which case was heard by the largest Constitution Bench of 13 judges of the Supreme Court till date?",
     "Golaknath Case", "Ashok Kumar Thakur Case", "Shah Bano Case", "Kesavananda Bharti Case", 4],

    ["XIV] Under which of the following Indian Constitution is it allowed to participate in the proceedings of Parliament?",
     "Solicitor General", "Attorney General", "Cabinet Secretary", "Chief Justice", 2],

    ["XV] What was the name given to the supercluster of galaxies discovered by Indian astronauts in the year 2017?",
     "Lakshmi", "Parvati", "Saraswati", "Durga", 3],

    ["XVI] Which of these colonial power ended its participation by selling the rights of Nicobar Island to the British on 18 October 1868?",
     "Belgium", "Italy", "France", "Denmark", 4],

    ["XVII] What is the name of the first person to be born in Antarctica?",
     "Emilio Palma", "James Waddell", "Charles Vicky", "James Wadley", 1]
]

level = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,
         320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]
# level 1 : V (4) [10,000]
# level 2 : X (9) [3,20,000]
# level 3 : XV (14) [75,00,000]
# level 4 : XVII (16) [7,50,00,000]

progress_money = []
won_money = [0]

for i in range(len(questions)):
    question = questions[i]
    print(question[0])
    print("\n")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    print("\n")
    ans = int(input("Enter Your Choice : "))

    if ans == question[-1]:
        print("Correct Answer !!!")
        progress_money = level[i]
        print(f"You've Won Rs. {progress_money}")
        print("\n")
        if progress_money == level[4]:
            won_money.pop(0)
            won_money.append(level[4])
        if progress_money == level[9]:
            won_money.pop(0)
            won_money.append(level[9])
        if progress_money == level[14]:
            won_money.pop(0)
            won_money.append(level[14])
        if progress_money == level[16]:
            won_money.pop(0)
            won_money.append(level[16])
            print(" You've Won Rs. 7.5 Crore !!!!")
            break
    else:
        print("Wrong Answer !!!")
        print("Your Won Money is Rs.", won_money[0], "!!!")
        break

print("\n")
