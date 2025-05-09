import re
import random
from .utils import swap_punctuation

def search_keywords(message, num_keywords, keywords):
    """
    Search for keyword occurrences in the message and return their locations.

    Args:
    - message (str): The message to search for keywords in.
    - num_keywords (int): The number of keywords to search for.
    - keywords (list): List of keywords to search for.

    Returns:
    - list: List of tuples containing keyword index and location in the message.
    """
    locations = []
    
    for i in range(num_keywords):
        current_message = message
        keyword = keywords[i].upper()
        match = re.search(r"\b" + re.escape(keyword) + r"\b", current_message.upper())
        
        while match is not None:
            locations.append((i, match.start()))
            current_message = current_message[match.end():]
            match = re.search(r"\b" + re.escape(keyword) + r"\b", current_message.upper())
    
    return locations

def perform_swaps(swaps, message):
    """
    Swap the keywords in the response to complete the bot's output.

    Args:
    - swaps(dict): A dictionary that shows possible swaps between words
    - message (str): The message to perform swaps on.

    Returns:
    - str: The message with keywords swapped according to predefined patterns.
    """
    keys = list(swaps.keys())
    
    # Get the indexes where swap words are in the message
    locations = search_keywords(message, len(keys), keys)
    
    response = message.upper()
    
    for location in locations:
        key = keys[location[0]]
        value = swaps[key]
        response = re.sub(r"\b" + re.escape(key) + r"\b", value, response)
    
    response = re.sub(r"(\.)|(\?)", swap_punctuation, response)
    return response
        
def build_response(data, message, locations, keywords):
    """
    Builds a response based on the user's message, keyword locations, and available patterns.

    Args:
    - data(dict): The data stored in the JSON file
    - message (str): The user's input message.
    - locations (list): List of tuples representing the locations of keywords in the message.
    - keywords (list): List containing keyword patterns.

    Returns:
    - str: The built response based on the message, keyword locations, and patterns.
    """
    responses = data['keyword-responses']
    response = ""
    current_index = 0
    
    # Sort the locations list to ensure responses are built from the beginning of the user's sentence
    locations = sorted(locations, key=lambda x: x[1])

    for keyword_index, end_index in locations:
        base_response = responses[keywords[keyword_index]][random.randint(0, data['responsesPerKeyword'][keyword_index] - 1)]
        
        # Find the start index of the keyword in the message
        start_index = current_index
        while current_index < end_index:
            current_index += 1

        # Build response by appending swapped message and base response
        swapped_message = perform_swaps(data['swaps'], message[start_index:end_index])
        response += swapped_message + base_response + " "

        # Move current index to end of keyword
        current_index = end_index + len(keywords[keyword_index])

    # Append any remaining part of the message after the last keyword
    response += perform_swaps(data['swaps'], message[current_index:])
    return response