import webbrowser
import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("coice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning Pulkit sir..")

    if hour >= 12 and hour < 16 :
        speak("Good Afternoon Pulkit sir..")

    if hour >= 16 and hour < 19 :
        speak("Good Evening Pulkit sir..")

    if hour >=19 and hour < 24 :
        speak("Good Morning Pulkit sir..")

    speak("My name is jarvis I am your personal assistan. Please tell me  How may I help you ...")

def take_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # code should wait for 1 sec befoore next phase
        r.pause_threshold=1
        audio=r.listen(source)

    try :
        print("Recognising...")
        querry=r.recognize_google(audio,language="en-in")
        print("User said: ",querry)
    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"

    return querry





if __name__=="__main__":
    wish_me()
    while True:
        audio=take_command().lower()
        if "wikipedia" in audio:
            speak("Searching wikipedia..")
            audio.replace("wikipedia","")
            result = wikipedia.summary(audio,sentences=2)
            speak(result)

        elif "open youtube" in audio:
            speak("Opening Youtube..")
            webbrowser.open("youtube.com")

        elif "open gmail" in audio:
            speak("Opening gmail..")
            webbrowser.open("gmail.com")

        elif "open chat gpt" in audio:
            speak("Opening chatgpt..")
            webbrowser.open("https://chat.openai.com/")

        elif "open google" in audio:
            speak("Opening chatgpt..")
            webbrowser.open("google.com")

        elif "play music" in audio:
            speak("Opening chatgpt..")
            webbrowser.open("youtube.com")

        elif "the time" in audio:
            tm= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {tm}")

        elif "open code" in audio:
            path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.1\\bin\\pycharm64.exe"
            os.startfile(path)

        elif "shutdown" in audio:
            exit()

