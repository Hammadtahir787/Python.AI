import os
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import psutil
import platform
import subprocess
import google.generativeai as genai

# === Setup Gemini API ===
genai.configure(api_key="AIzaSyAiqzAcK0L2cm_H4mc-oR6SBIfZQEoWHDg")  # Replace this with your actual key
model = genai.GenerativeModel("gemini-1.5-flash")


# Initialize speech tools
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
        speak("Please check your internet connection.")
        return ""

def get_pc_specs():
    cpu = psutil.cpu_freq()
    mem = psutil.virtual_memory()
    os_info = platform.system() + " " + platform.release()
    return f"OS: {os_info}, CPU: {cpu.current:.0f} MHz, RAM: {round(mem.total / (1024**3), 2)} GB"

def get_time_day():
    now = datetime.datetime.now()
    return f"Today is {now.strftime('%A')}, and the time is {now.strftime('%I:%M %p')}."

def open_word():
    paths = [
        r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
    ]
    for path in paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return True
    return False

def gemini_reply(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error from Gemini: {e}"

def process_command(cmd):
    if "youtube" in cmd:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "google" in cmd:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "whatsapp" in cmd:
        speak("Opening WhatsApp Web.")
        webbrowser.open("https://web.whatsapp.com")
    elif "specs" in cmd or "computer" in cmd:
        speak(get_pc_specs())
    elif "time" in cmd or "day" in cmd:
        speak(get_time_day())
    elif "word" in cmd:
        if open_word():
            speak("Opening Microsoft Word.")
        else:
            speak("I couldn't find Microsoft Word installed.")
    elif any(q in cmd for q in ["how are you", "what's up", "hello", "hi"]):
        speak("I'm doing great. How can I help you?")
    elif any(q in cmd for q in ["who are you", "what can you do"]):
        speak("I'm your voice assistant. I can open apps, browse the web, and answer your questions using AI.")
    elif "exit" in cmd or "quit" in cmd:
        speak("Goodbye!")
        exit()
    else:
        speak("Let me think...")
        reply = gemini_reply(cmd)
        speak(reply)

# === MAIN LOOP ===
speak("Voice assistant is ready.")
while True:
    command = listen()
    if command:
        process_command(command)
