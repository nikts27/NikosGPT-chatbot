# main.py

import re
from chatbot.config import load_data
from chatbot.core import build_response, search_keywords
from chatbot.utils import return_generic_response

def main():
    print("NikosGPT: Hello, I am NikosGPT, an AI chatbot. How can I help you today?")
    print("(Type bye to finish conversation)")

    data = load_data()
    keywords = list(data['keyword-responses'].keys())

    while True:
        user_input = input("You: ")
        if re.search('BYE', user_input.upper()):
            break

        keyword_locations = search_keywords(user_input, len(keywords), keywords)
        if keyword_locations:
            response = build_response(data, user_input, keyword_locations, keywords)
        else:
            response = return_generic_response(data['generic-responses'], user_input)

        print("NikosGPT: " + response.capitalize())
    print("NikosGPT: Have a nice day!!! :-)")

if __name__ == "__main__":
    main()