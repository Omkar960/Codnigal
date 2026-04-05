import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator
def speak(text,lang="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    voices = engine.getProperty("voices")
    for voice in voices:
        if lang in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now in English")
        audio = recognizer.listen(source)
    try:
        print("Recognizing speech")
        text = recognizer.recognize_google(audio)
        print(f"You said {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f" API error {e}")
    return ""
def translate_text(text, target_language="hi"):
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    print(f"🌍 Translated text: {translated}")
    return translated
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
    return languagedict.get(choice)
def main():
    targetlanguage = displaylangoptions()
    originaltext = speech_to_text()
    if originaltext:
        translatedtext = translate_text(originaltext,targetlanguage)
        speak(translatedtext,targetlanguage)
        print("Translation spoken out!")
if __name__ == "__main__":
    main()