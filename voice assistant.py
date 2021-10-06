import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your voice assistant how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"User said: {text}\n")

    except Exception as e:
        # print(e)
        speak("please repeat again...")
        return "None"
    return text


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        text = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'open youtube' in text:
            webbrowser.open("youtube.com")

        elif 'open google' in text:
            webbrowser.open("google.com")

        elif 'who is' in text:
            person = text.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'how are you' in text:
            speak("im good, thanks for asking")

        elif 'play' in text:
            song = text.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in text:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'joke' in text:
            speak(pyjokes.get_joke())

        elif 'name' in text:
            speak("prajwal")

        elif 'exit' in text:
            speak("thank you")
            quit()
