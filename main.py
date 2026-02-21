import speech_recognition as sr
import webbrowser
import musicLibrary
import pyttsx3
import time
import requests
import os

r = sr.Recognizer()
newsapi="" #Insert your key here
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:7b"

# System prompt
system_prompt = {
    "role": "system",
    "content": (
        "You are Orion, an AI assistant for serious Q&A, reasoning, general knowledge, "
        "casual talking, and problem-solving. "
        "You understand English, Hindi, and Hinglish. "
        "Answer clearly and concisely. Avoid vague replies."
    )
}

# Conversation memory
messages = [system_prompt]

def aiProcess(command,max_tokens=200):
    global messages

    # Add user input
    messages.append({"role": "user", "content": command})

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.5,
            "top_p": 0.95,
            "num_predict": max_tokens,
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    reply = response.json()["message"]["content"].strip()

    # Save assistant reply
    messages.append({"role": "assistant", "content": reply})

    # Keep last 10 messages only (memory control)
    messages = messages[-10:]

    speak(reply)     # your TTS function
    return reply

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/CodeWithShrey-collab")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"): 
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        response=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if response.status_code==200:
            #parse the json repsonse
            data=response.json()

            #extract the articles
            articles=data.get('articles',[])

            #print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let AI handle the request
        output=aiProcess(c)
        speak(output)

print("Initializing Orion")
speak("Initializing Orion")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=3)

        word = r.recognize_google(audio)
        print("Heard:", word)

        if "orion" in word.lower():
            time.sleep(0.4)   # 👈 critical
            speak("Yes")

            with sr.Microphone() as source:
                print("Listening for command...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            command = r.recognize_google(audio)
            print("Command:", command)
            processCommand(command)
            
    except Exception as e:
        print("Error:", e)
