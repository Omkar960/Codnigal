import threading
import sys
import time
try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import wave
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f" Missing library {e.name}")
    print("\n???? Install commands.")
    print(" Windows: pip install SpeechRecogntiion pyaudio numpy matplotlib")
    print(" macOS: brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")
    sys.exit(1)
stop_event = threading.Event()

def waitforeneter():
    input("\n Presse neter to stop recording... ")
    stop_event.set()
def spinner():
    chars = "|/-\\"
    i = 0 
    while not stop_event.is_set():
        sys.stdout.write(f"\r???? Recording... {chars[i%4]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print(" Recording Complete. ")
def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000, input=True,frames_per_buffer=1024)
    frames = []

    threading.Thread(target=waitforeneter,daemon=True).start()
    threading.Thread(target=spinner,daemon=True).start()

    while not stop_event.is_set():
        frames.append(stream.read(1024,exception_on_overflow=False))
        

