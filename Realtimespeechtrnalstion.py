import pyttsx3
import speech_recognition as sr
import os
import time
from deep_translator import GoogleTranslator
import pygame
import music
from gtts import gTTS

def speak(text,language="hi"):
    try:
        filename = "translatedvoice.mp3"
        tts = gTTS(text=text,lang=language)
        tts.save(filename)
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.quit()
        os.remove(filename)
    except Exception as e:
        print(f"Error in speaking:{e}" )
def speechtotext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now in English...")
        audio = recognizer.listen(source)
    try:
        print('??? Recognizing speech...')
        text = recognizer.recognize_google(audio,language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API error: {e}")
    return ""
def translatetext(text,target_language="hi"):
    translation = GoogleTranslator(source="auto",target=target_language).translate(text)
    print(f"Translated Text: {translation}")
    return translation
def displaylangoptions():
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
    return languagedict.get(choice,"es")
def main():
    target_language = displaylangoptions()
    originaltext = speechtotext()
    if originaltext:
        translatedtext = translatetext(originaltext,target_language=target_language)
        speak(translatedtext,language=target_language)
        print("Translation spoekn out")
if __name__ == "__main__":
    main()