import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator
engine = pyttsx3.init(driverName='nsss')
engine.setProperty("rate",150)
def speak(text,language="en"):
    engine.say(text)
    engine.runAndWait()
def speechtotext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now in English...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
    try:
        print("??? Recognizing speech...")
        text = recognizer.recognize_google(audio,language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API error: {e}")
    return ""
def translatetext(text,targetlanguage="hi"):
    try:
        translated = GoogleTranslator(source="auto",target=targetlanguage).translate(text)
        print(f" Translated Text:{translated}")
        return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return ""
def displaylanguageoptions():
    print("\n Available languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    choice = input("Select language (1-8): ")
    languagedict = {"1":"hi","2":"ta","3":"te","4":"bn","5":"mr","6":"gu","7":"ml","8":"pa"}
    return languagedict.get(choice,"hi")
def main():
    targetlanguage = displaylanguageoptions()
    originaltext = speechtotext()
    if originaltext:
        translatedtext = translatetext(originaltext,targetlanguage)
        if translatedtext:
            speak(translatedtext)
            print("Done")
if __name__ == "__main__":
    main()

