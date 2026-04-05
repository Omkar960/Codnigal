import pyttsx3
import speech_recognition as sr
from datetime import datetime
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()
def getaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("??? Speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print(f"API Error: {e}")
    return ""
def respondtocommand(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I am you Python voice assistant.")
    elif "my name is" in command:
        username = command.split("my name is")[-1].strip().capitalize()
        speak(f"Nice to meet you {username}")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"Time is {now}")
    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    elif "fact" in command:
        facts = [" Honey never spoils. Archaeologists found 3000-year old honey in Egyptian tombs!", "Octopuses have three hearts","Bananas are berries, but strawberries aren't.","The Eiffel Tower can grow taller in the summer.","Water can boil and freeze at the same time in a vacuum."]
        speak(random.choice(facts))
    elif "use male voice" in command:
        engine.setProperty('voice',voices[0].id)
        speak("Changed to male voice")
    elif "use female voice" in command:
        engine.setProperty('voice',voices[1].id)
        speak("Switched to female voice.")

    else:
        speak("I'm not sure how I can help you with that")
    return True
def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = getaudio()
        if command and not respondtocommand(command):
            break
if __name__ == "__main__":
    main()
