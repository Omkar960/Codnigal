import sys
import threading

try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import wave
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f" ❌ Missing library: {e.name}")
    print("\n??? Install commands.")
    print(" Windows: pip install Speech Recogntion pyaudio numpt matplotlib")
    print(" macOS: brew install portaduio and pipe install SpeechRecogntion pyaudio numpt matplotlib")
    sys.exit(1)
stop_event = threading.Event()
def waitforenter():
    input()
    stop_event.set()
def recordaudio(label):
    stop_event.clear()
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=1024)
    frames = []
    print(f"/n??? {label}")
    print(" Press Enter to stop...")
    threading.Thread(target=waitforenter,daemon=True).start()
    print("??? Recording",end="",flush=True)
    while not stop_event.is_set():
        frames.append(stream.read(1024,exception_on_overflow=False))
        print(".",end="",flush=True)
    print("✅")
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames),16000, width
def analyzeaudio(data,rate):
    sample = np.frombuffer(data,dtype=np.int16)
    return { 'duration': len(sample)/rate,'avg_volume': np.mean(np.abs(sample)), 'max_volume': np.max(np.abs(sample)),
    'samples':sample}
def transcribe(data,rate,width):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(AudioData(data,rate,width))
    except:
        return "[Could not transribe]"
def displaystats(stats,text,label):
    print(f"\n{{'-'(40)}}")
    print(f"??? {label}")
    print(f"\n{{'-'(40)}}")
    print(f" Duration: {stats['duration']:.2f} seconds")
    print(f"??? Avg Amplitude: {stats["avg_volume"]}")
    print(f"??? Max Amplitude: {stats["max_volume"]}")
    print(f"???? Transcription: {text}")
def compare(stats1,stats2):
    print(f"\n"+"="*40)
    print("???? COMPARISON RESULTS")
    print("="*40)
    if stats1['duration'] > stats2['duration']:
        longer = "Recording 1"
        diff = ((stats1['duration']-stats2['duration'])/stats2['duration']*100)
    else:
        longer = "Recording 2"
        diff = ((stats2['duration']-stats1['duration'])/stats1['duration']*100)
    print(f" {longer} is longer by {diff:.1f}%")
    if stats1[""]