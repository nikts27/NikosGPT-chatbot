# chatbot/config.py

import json

def load_data(json_path='keywords.json'):
    with open(json_path) as f:
        return json.load(f)
