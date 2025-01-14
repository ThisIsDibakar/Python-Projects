import time

print("\n")

timestamp = time.strftime('%H:%M:%S')
print("Time: ", timestamp)

if int(time.strftime('%H')) >= 0 and int(time.strftime('%H')) < 12:
    print("WOW, it's Morning 🤪!!!")
    print("Good Morning Human!!!")

elif int(time.strftime('%H')) >= 12 and int(time.strftime('%H')) < 18:
    print("Ahh, it's still Afternoon 🫠!!!")
    print("Good Evening Human!!!")

else:
    print("LOL, it's Night 🥱!!!")
    print("Good Night Human")

print("\n")
