# 🗣️ AI Voice Assistant using Python

A personal AI-powered Voice Assistant that listens to your voice commands, responds with human-like speech, and performs tasks such as opening websites, launching applications, searching the internet, and more.

---

## 🚀 Features

- 🎤 Voice input (Speech-to-Text)  
- 🗣️ Voice output (Text-to-Speech)  
- 🌐 Open websites (Google, YouTube, etc.)  
- 📞 Simulated call and messaging  
- 📅 Provides current time and date  
- 🔁 Execute custom commands  
- 📦 Local database support (SQLite or JSON)  
- 📁 File and folder operations  
- 🔊 Works both offline (with `pyttsx3`) and online (with `gTTS`)  

---

## 🛠️ Technologies Used

| Category       | Tools/Libraries                  |
| -------------- | ------------------------------- |
| Programming    | Python 3.x                       |
| Voice Input    | `speech_recognition`             |
| Voice Output   | `pyttsx3`, `gTTS`                |
| Audio Handling | `pyaudio`, `playsound`           |
| Web Control    | `webbrowser`, `requests`         |
| Time & Date    | `datetime`, `time`               |
| Database       | `sqlite3`, `json`                |
| Others         | `os`, `subprocess`, `platform`   |

---

## 📦 Setup & Installation 

### Prerequisites

- Python 3.x installed: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Install Required Libraries

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```


---

## 📁 Folder Structure

```
voice-assistant/
├── main.py                 # Main application logic
├── commands.py             # (Optional) Command handling module
├── database/               # Data storage files (JSON or SQLite DB)
│   └── user_data.json or sqlite.db
├── assets/                 # Icons, audio files, etc.
├── requirements.txt        # Dependency list
├── README.md               # This file
```


---

## 🧪 How to Run

1. Clone the repository:

```bash
git clone https://github.com/shivacharandhoni/voice-assistant.git
```

2. Navigate into the project directory:

```bash
cd voice-assistant
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the assistant:

```bash
python main.py
```


---

## 🔗 Useful Links

- [Official Python Website](https://www.python.org/)
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3 Documentation](https://pypi.org/project/pyttsx3/)
- [Voice Assistant GitHub Repo](https://github.com/shivacharandhoni/voice-assistant)

---

## 👨‍💻 Author

**Shivacharan Dhoni**

📧 [shivacharandhoni@gmail.com](mailto:shivacharandhoni@gmail.com)

🌐 [GitHub Profile](https://github.com/shivacharandhoni)

---


