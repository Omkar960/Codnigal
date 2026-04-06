import asyncio
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

LANGUAGE_OPTIONS = {
    "1": ("Hindi", "hi"),
    "2": ("Tamil", "ta"),
    "3": ("Telugu", "te"),
    "4": ("Bengali", "bn"),
    "5": ("Marathi", "mr"),
    "6": ("Gujarati", "gu"),
    "7": ("Malayalam", "ml"),
    "8": ("Punjabi", "pa"),
}

def speak(text:str,language:str = "en") -> None:
    engine = pyttsx3.init()
    engine.setProperty("rate",150)
    voices = engine.getProperty("voices")
    if voices:
        if language == "en":
            engine.setProperty("voice",voices[0].id)
        elif len(voices) > 1:
            engine.setProperty("voice",voices[1].id)
    engine.say(text)
    engine.runAndWait()
def speechtotext() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n Please speak now in English...")
        recognizer.adjust_for_ambient_noise(source,duration=0.7)
        audio = recognizer.listen(source)
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio,language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as exc:
        print(f"Speech API Error: {exc}")
    return ""
async def translatetext(text: str, target_language: str) -> str:
    translator = Translator()
    translation = await translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text

def display_language_options() -> tuple[str, str]:
    print("\nAvailable translation languages:")
    for key, (name, code) in LANGUAGE_OPTIONS.items():
        print(f"{key}. {name} ({code})")
    while True:
        choice = input("Please select the target language number (1-8): ").strip()
        if choice in LANGUAGE_OPTIONS:
            return LANGUAGE_OPTIONS[choice]
        print("Invalid selection. Please enter a number from 1 to 8.")

def run_translator() -> None:
    target_name, target_code = display_language_options()
    print(f"\nTarget language selected: {target_name} ({target_code})")
    original_text = speechtotext()
    if not original_text:
        print("No speech was recognized. Returning to the main menu.")
        return
    translated_text = asyncio.run(translatetext(original_text, target_code))
    print("Speaking translated output...")
    speak(translated_text, language="en")
    print("Translation spoken out!")
def main() -> None:
    print("===== AI Voice Translator Console =====")
    while True:
        print("\n1. Start voice translation.")
        print("2. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            run_translator()
        elif choice == "2":
            print("Exiting translator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()