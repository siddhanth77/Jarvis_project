# Jarvis Voice Assistant

A desktop personal assistant inspired by the fictional Jarvis system. This project listens for a wake word, recognizes voice commands, speaks responses using text-to-speech, and can open websites, play music, fetch news, capture screenshots, and answer general questions with an AI backend.

## Overview

This project combines:

- Voice input using SpeechRecognition
- Text-to-speech using pyttsx3
- Browser automation via webbrowser
- Music links from a custom dictionary
- News headlines from NewsAPI
- Screenshot capture using pyautogui
- AI-powered responses through the Groq/OpenAI-compatible API

The main entry point is `main.py`, which runs a loop that waits for the wake word "Jarvis" and then listens for a command.

---

## Project Structure

- `main.py` – main assistant logic and voice command workflow
- `musicLibrary.py` – dictionary of music/video links for predefined songs
- `screenshot.py` – helper script to capture a screenshot instantly
- `client.py` – quick API test script for the Groq/OpenAI client
- `code.py` – older/experimental version of the project with commented code and a prototype flow

---

## Features

### Voice assistant commands

The assistant recognizes commands such as:

- "Jarvis open google"
- "Jarvis open youtube"
- "Jarvis open chatgpt"
- "Jarvis play skyfall"
- "Jarvis what time is it"
- "Jarvis tell me the date"
- "Jarvis take screenshot"
- "Jarvis news"
- "Jarvis stop"

### Built-in functionality

- Opens common websites in the default browser
- Plays selected songs by opening a YouTube link from `musicLibrary.py`
- Tells the current time and date
- Fetches top news headlines from NewsAPI
- Captures the full screen and saves it to `OneDrive/Desktop/Jarvis screenshot`
- Falls back to an AI response when a command is not recognized

### AI support

The assistant uses Groq via the OpenAI-compatible endpoint:

- `api_key=os.environ.get("GROQ_API_KEY")`
- `base_url="https://api.groq.com/openai/v1"`

This allows the assistant to answer broader questions when a command does not match built-in actions.

---

## How It Works

1. The app starts and speaks a greeting.
2. It listens to microphone input.
3. If the spoken text contains "jarvis", it activates the assistant.
4. It records the next command.
5. The command is processed by `processCommand()`.
6. Depending on the text, it:
   - opens a site,
   - reads a song URL,
   - fetches news,
   - captures a screenshot,
   - speaks time/date,
   - or sends the query to Groq AI.

---

## Installation

### 1. Clone the project

```bash
git clone <your-repository-url>
cd "The jarvis project"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file or set the environment variable in your terminal:

```bash
set GROQ_API_KEY=your_groq_api_key
```

On macOS/Linux:

```bash
export GROQ_API_KEY=your_groq_api_key
```

> Important: the project currently keeps a NewsAPI key directly in `main.py`. This should be moved to an environment variable for security and flexibility.

---

## Required Dependencies

The project relies on:

- `SpeechRecognition`
- `pyttsx3`
- `requests`
- `openai`
- `pyautogui`
- `PyAudio`

See `requirements.txt` for the exact package list.

---

## Run the Project

```bash
python main.py
```

Then say:

```text
Jarvis
```

Followed by a command such as:

```text
open google
```

---

## Example Commands

- "Jarvis open google"
- "Jarvis open youtube"
- "Jarvis play skyfall"
- "Jarvis what time is it"
- "Jarvis tell me the date"
- "Jarvis give me the news"
- "Jarvis screenshot"
- "Jarvis stop"

---

## Notes and Limitations

### Microphone support

`SpeechRecognition` depends on microphone access. On Windows, you may need to install `PyAudio` successfully before voice capture works.

### Audio engine

`pyttsx3` uses the system's installed TTS engine. Some machines may require additional voice packages or OS-level speech support.

### API security

The current code stores sensitive values such as the NewsAPI key as a literal string in the code. It is better practice to move those into environment variables or a `.env` file.

### Browser and screenshot behavior

- The app opens links directly in the default browser.
- Screenshot files are saved under the user's desktop folder in a `Jarvis screenshot` directory.

---

## Suggested Improvements

- Move the NewsAPI key and other secrets to environment variables
- Improve command parsing and wake-word processing
- Add a proper command dictionary and intent detection system
- Add more actions like email, file search, weather, and reminders
- Support a GUI or web dashboard
- Add error handling for missing microphone or speech recognition failures
- Clean up `code.py` and remove stale/duplicate prototype code

---

## Summary

This is a functional voice assistant prototype that demonstrates a real desktop AI assistant workflow. It is suitable for learning, prototyping, and extending into a more advanced personal assistant project.

---

## License

This project is currently unlicensed unless you add one explicitly.

If you want, you can add a license such as MIT or Apache 2.0.
