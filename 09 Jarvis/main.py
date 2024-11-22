import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
client = OpenAI(api_key="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")


engine = pyttsx3.init()
newsAPI = "9e5be233efeb45719ded679e3f979771"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message

def processCommand(c):
    # Print the command
    print(f"You Said: {c}")

    # Open Google or YouTube
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    # Play music from the library
    elif c.lower().startswith("play"):
        song = c.split(" ")[1].strip()
        if song.lower() in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            speak(f"Playing {song} from the library")
        else:
            speak("I'm sorry, I couldn't find that song in the library.")

    # Search for news
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPI}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            articles = data["articles"]
            for i, article in enumerate(articles):
                speak(f"News {i+1}: {article['title']}")
                webbrowser.open(article["url"])
                speak(f"Sure, I've opened the article for you. {article['title']}")

    # Let OpenAI Handle the request
    else:
        response = aiProcess(c)
        speak(response)


if __name__ == "__main__":
    speak("Initializing Jarvis ....")
    while True:
        # Obtain audio from the microphone
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening ....")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            # Recognize speech using Google
            word = r.recognize_google(audio)

            # Listen for the wake word "Jarvis"
            if word.lower() == "jarvis":
                speak("Yes, Boss")
                with sr.Microphone() as source:
                    print("Listening ....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    # Execute the command
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
