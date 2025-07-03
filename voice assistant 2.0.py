import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import psutil
import platform

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
def listen(duration=5, fs=16000):
    speak("Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    audio = np.squeeze(audio)

    try:
        audio_data = sr.AudioData(audio.tobytes(), fs, 2)
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        speak("Could not request results. Check your internet connection.")
        return ""

def get_pc_specs():
    cpu = psutil.cpu_freq()
    mem = psutil.virtual_memory()
    os_info = platform.system() + " " + platform.release()
    return f"OS: {os_info}, CPU: {cpu.current:.0f} MHz, RAM: {round(mem.total / (1024 ** 3), 2)} GB"

def get_time_day():
    now = datetime.datetime.now()
    return f"{now.strftime('%A')}, {now.strftime('%I:%M %p')}"

def process_command(cmd):
    if "youtube" in cmd:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "google" in cmd:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "whatsapp" in cmd:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")
    elif "specs" in cmd:
        speak(get_pc_specs())
    elif "time" in cmd or "day" in cmd:
        speak(get_time_day())
    elif "exit" in cmd or "quit" in cmd:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
speak("Voice assistant is ready.")
while True:
    command = listen()
    if command:
        process_command(command)
