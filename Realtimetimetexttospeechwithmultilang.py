import asyncio
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text,language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice',voices[0].id)
    else:
        engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
def speechtotext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now")
        audio= recognizer.listen(source)
    try:
        print("???? Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"You said {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""
def translatetext(text,target_language="es"):
    translator = Translator()
    translation = translator.translate(text,dest=target_language)
    if asyncio.iscoroutine(translation):
        translation = asyncio.run(translation)
    print(f"Translated text: {translation.text}")
    return translation.text
def displaylanguageoptions():
    print("\n Available languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Spanish (es)")
    print("5. French (fr)")
    choice = input("Select language (1-5): ")
    languagedict = {"1":"hi","2":"ta","3":"te","4":"es","5":"fr"}
    return languagedict.get(choice,'es')
def main():
    print("=== Real-Time Speech Translation===")
    target_language = displaylanguageoptions()
    original_text = speechtotext()
    if original_text:
        translatedtext = translatetext(original_text,target_language=target_language)
        speak(translatedtext,language=target_language)
        print("Translation spoken out!")
if __name__ == "__main__":
    main()


              
