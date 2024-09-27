# NikosGPT - A Keyword-based AI Chatbot

Welcome to **NikosGPT**, a keyword-based AI chatbot that can respond dynamically to user input using a combination of keyword recognition and message swapping. This project leverages Python, regular expressions, and JSON-based keyword mapping to create responses that adapt to user inputs.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Dynamic Responses**: The chatbot can provide context-aware responses by recognizing keywords in user input.
- **Customizable**: Easily update keywords, responses, and swap patterns by editing a JSON file.
- **Punctuation Swapping**: The bot can swap punctuation marks (like `.` and `?`) for more dynamic sentence flow.
- **Fallback Generic Responses**: If no keywords are matched, the bot provides a generic response from a predefined list.
- **Keyword Matching**: Utilizes regular expressions to find keyword occurrences and responds accordingly.

## How It Works

NikosGPT uses a keyword-based system to craft responses. The steps are:
1. **User Input**: The bot receives the user’s message.
2. **Keyword Search**: The program checks if any predefined keywords (stored in a JSON file) appear in the message.
3. **Response Generation**: If keywords are found, it builds a response by performing word swaps and applying a base response associated with the keyword.
4. **Punctuation Swap**: The program replaces punctuation marks like `.` with `?` for variety.
5. **Generic Response**: If no keywords are found, the bot uses a generic fallback response from a predefined list.
   
## Installation

### Requirements

- Python 3.6 or higher
- A JSON file containing the keywords and responses (See [keywords.json](#keywords-json-format))

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/NikosGPT.git
    cd NikosGPT
    ```

2. **Create Your `keywords.json` File** (See format below)

3. **Run the Script**:
    ```bash
    python nikos_gpt.py
    ```

## Usage

Once the bot starts, it will greet you with a message:

```bash
NikosGPT: Hello, I am NikosGPT, an AI chatbot. How can I help you today?
(Type bye to finish conversation)
```

You can type messages to interact with the bot. Type `bye` to end the conversation.
