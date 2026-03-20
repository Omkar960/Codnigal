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
    
    stream.stop_stream()

    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()

    return b''.join(frames), 160000, width
def saveaudio(data,rate,width,filename="recording.wav"):

    with wave.open(filename,"wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"??? Saved: {filename}")
    
def transcribe(data,rate,width):
    recognizer = sr.Recognizer()
    audio = AudioData(data,rate,width)
    try:
        text = recognizer.recognize_google(audio)
        print(f"??? Transcription: {text}")
    except sr.UnknownValueError:
        print(" Could not understand audio")
    except sr.RequestError as e:
        print(f" API error {e}")
def plotwaveform(data,rate):
    samples = np.frombuffer(data,dtype=np.int16)
    timeaxis = np.linspace(0,len(samples)/rate,len(samples))

    plt.figure(figsize=(10,4))
    plt.plot(timeaxis,samples,color="blue")
    plt.title("Your Voice Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.show()
def main():
    print('='*40)
    print("??? HELLO AI, CAN YOU HEAR ME")
    print("="*40)
    print("\n Speak into your microphone...")
audio_data,rate,width = record_audio()

saveaudio(audio_data,rate,width)
transcribe(audio_data,rate,width)
plotwaveform(audio_data,rate)
if __name__ == "__main__":
    main()