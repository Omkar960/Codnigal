import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate",150)
engine.setProperty("volume",0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def getsamples():

    return["Hello! I am your computer!","Pyhton is awesome!","This is AI speaking!","Welcome to the future!","Never give up on learning!","AI can be fun and helpful","Speak your thoughts into code!"]
def main():
    print("??? VOICE MASTER+")
    speak("Hello! Type something for me to say!")
    while True:
        userinput = input("\n??? You").strip().lower()
        if userinput.lower() == "exit":
            speak("Goodbye! See you next time. ")
            break
        elif userinput == "sample":
            phrase = random.choice(getsamples())
            print(f"??? {phrase}")
            speak(phrase)
        elif userinput == "speed up":
            rate = engine.setProperty("rate",rate)
            speak(f"Speaking faster now at {rate} rate")
        elif userinput == "slow down":
            rate = engine.getProperty("rate") - 50
            speak(f"Speaking slow now at {rate} rate.")
        elif userinput == "increase volume":
            vol = engine.getProperty("volume") + 0.1
            vol = min(1.0,vol)
            engine.setProperty("volume",vol)
            speak("Volume increased")
        elif userinput == "decrease volume":
            vol = engine.getProperty("volume") - 0.1
            vol = max(0.0,vol)
            engine.setProperty("volume",vol)
            speak("Volume decreased.")
        elif userinput == "tell a joke":
            joke = ["Why don't scientist trust atoms? They make up everything!", "What do you call fake spaghetti? An impasta!", "I told my computer I needed a break, and it said: 'No problem, I'll go back to sleep!' "]
            joke = random.choice(joke)
            print(f"??? {joke}")
            speak(joke)
        elif userinput:
            speak(userinput)
        else:
            print("??? Type 'sample','tell a joke', or 'exit' ")
            speak("I didn't quite catch that. Try again!")
if __name__ == "__main__":
    main()