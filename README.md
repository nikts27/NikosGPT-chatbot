# NikosGPT - A Keyword-based AI Chatbot

Welcome to **NikosGPT**, a lightweight AI chatbot built in Python that generates dynamic responses based on user input using keyword matching and message transformation. It’s designed to be customizable, modular, and easily extendable.

> ⚡ Inspired by early natural language systems like ELIZA — built for modern learning and experimentation.

---

## 📑 Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Keywords JSON Format](#keywords-json-format)
- [Demo](#demo)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 🚀 Features

- **Dynamic Response Generation**: Uses keyword mapping and word swapping to form contextual replies.
- **Configurable Behavior**: Modify keywords, patterns, and responses in a single JSON file — no code required.
- **Punctuation Swapping**: Automatically transforms punctuation (e.g. `.` ↔ `?`) to simulate conversational tone.
- **Fallback System**: When no match is found, the bot offers helpful generic responses.
- **Modular Codebase**: Clean separation of core logic, utilities, and configuration.

---

##⚙️ How It Works

1. **User Input**: The user types a message.
2. **Keyword Matching**: The bot scans the message using regular expressions.
3. **Message Transformation**: It swaps relevant words based on a predefined `swaps` dictionary.
4. **Response Construction**: A response is selected from a keyword-mapped list and merged into a reply.
5. **Fallback Response**: If no keywords match, a generic message is used.

---

## 🗂️ Project Structure

```
NikosGPT/
├── chatbot/
│   ├── core.py            # Chatbot logic (response generation, swapping)
│   ├── config.py          # Keyword JSON loader
│   └── utils.py           # Helpers (generic responses, punctuation swap)
├── data/
│   └── keywords.json      # Customizable behavior definitions
├── main.py                # Entry point for the chatbot
├── requirements.txt       # Dependencies
└── README.md              # Documentation (this file)
```

---

## 📥 Installation

### Requirements

- Python 3.6 or higher
- Git (optional, for cloning)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/NikosGPT-chatbot.git
   cd NikosGPT-chatbot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Chatbot**
   ```bash
   python main.py
   ```

---

## 💬 Usage

Once started, the chatbot will greet you:

```
NikosGPT: Hello, I am NikosGPT, an AI chatbot. How can I help you today?
(Type bye to finish conversation)
```

You can then type messages like:
- `Can you help me?`
- `I feel sad`
- `Why don't you listen?`

Type `bye` to exit.

---

## 🧠 Keywords JSON Format

Example structure of `keywords.json`:

```json
{
  "keyword-responses": {
    "I AM SAD": ["WHY DO YOU FEEL THAT WAY?", "DO YOU WANT TO TALK ABOUT IT?"]
  },
  "responsesPerKeyword": [2],
  "swaps": {
    "I": "YOU",
    "YOU": "I"
  },
  "generic-responses": [
    "I'M NOT SURE I FOLLOW — WANT TO REPHRASE?"
  ]
}
```

This makes it easy to extend the bot without touching the code.

---

## 🔭 Future Improvements

- Add Flask or FastAPI web interface
- Support for sentence-level sentiment analysis
- Conversation history & memory
- Expand keyword detection with synonyms (via NLTK or spaCy)
- Add unit tests and CI integration (e.g., GitHub Actions)

---

## 👤 Author

Created by Nikolaos Tsaridis(https://github.com/nikts27)

If you like this project or want to collaborate, feel free to connect on [LinkedIn](https://www.linkedin.com/in/ntsaridis/)) 

---

🧠 _This project was created for the first assignment of the course "Theory of Computation." (Applied Informatics, UoM, 3rd year)!_
