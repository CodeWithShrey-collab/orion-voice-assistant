# 🧠 Orion – Voice Assistant (Python + Ollama)

Orion is a lightweight Python-based voice assistant that listens for the wake word **"Orion"**, processes voice commands, and generates intelligent responses using a locally running Large Language Model via Ollama (`qwen2.5:7b`).

This project demonstrates practical integration of:

- Speech Recognition  
- Text-to-Speech  
- Local LLM APIs  
- Command Routing  
- External API Integration  
- Conversation Memory Handling  

---

## ✨ Features

- Wake word detection: **"Orion"**
- Voice-to-text using Google Speech Recognition
- Text-to-speech responses using `pyttsx3`
- Opens websites (Google, YouTube, GitHub, ChatGPT)
- Plays songs from a custom music library
- Fetches top headlines using NewsAPI
- Local AI-powered responses using Ollama (`qwen2.5:7b`)
- Maintains short-term conversation memory (last 10 exchanges)

---

## 📁 Project Structure
orion-voice-assistant/
│
├── main.py
├── musicLibrary.py
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Requirements

- Python 3.10 or higher
- Working microphone
- Internet connection (for Speech Recognition and NewsAPI)
- Ollama installed locally

---

# 🚀 Installation & Setup

---

## 1️⃣ Install Python

Download Python from:  
https://www.python.org/downloads/

During installation:
- ✅ Ensure **“Add Python to PATH”** is checked

Verify installation:
python --version


---

## 2️⃣ Install Ollama

Download Ollama from:  
https://ollama.com/download

Verify installation:
ollama --version


---

## 3️⃣ Download the Required AI Model

You do **NOT** need to manually download models from Hugging Face.

Simply run:
ollama pull qwen2.5:7b


Ollama will automatically:
- Download the model
- Store it locally
- Serve it at `http://localhost:11434`

Verify:
ollama list

You should see:
qwen2.5:7b
---

## 4️⃣ Clone the Repository
git clone https://github.com/CodeWithShrey-collab/orion-voice-assistant.git
cd orion-voice-assistant

## 5️⃣ Create Virtual Environment

### Windows
python -m venv .venv
..venv\Scripts\activate


### Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

---
## 6️⃣ Install Dependencies
pip install -r requirements.txt

If PyAudio fails on Windows:
pip install pipwin
pipwin install pyaudio


---

## 7️⃣ (Optional) Setup News API Key

Get a free API key from:  
https://newsapi.org

---

## 8️⃣ Ensure Ollama Is Running

In a separate terminal:
ollama serve

(Default endpoint: `http://localhost:11434`)

---

## 9️⃣ Run Orion
python main.py

Say:

> Orion

Then speak your command.

---

## 🎤 Example Commands

- Open Google  
- Open YouTube  
- Play arijit  
- News  
- Explain what is a stack  
- Who is Alan Turing  

---

## 🧠 How It Works

1. Microphone listens continuously for the wake word.
2. SpeechRecognition converts speech to text.
3. Predefined commands are handled directly.
4. All other queries are sent to Ollama via HTTP API.
5. The local LLM generates a response.
6. The response is converted to speech using pyttsx3.
7. The last 10 conversation messages are stored for context.

---

## ⚠️ Notes

- SpeechRecognition requires internet (Google API).
- Ollama runs locally, so AI responses work offline after the model is downloaded.
- The news feature requires a valid NewsAPI key.
- Designed for educational, experimentation, and portfolio purposes.

---

## 🔮 Future Improvements

- Graphical User Interface (GUI)
- Offline speech recognition engine
- Enhanced wake-word detection
- Command history logging
- Multi-language support
- Mobile or web companion interface

---

## 📄 License

This project is open-source and available under the MIT License.
