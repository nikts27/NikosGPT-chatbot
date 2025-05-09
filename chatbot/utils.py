# chatbot/utils.py

import re
import random

def swap_punctuation(match):
    """
    Swap punctuation marks in the message.

    Args:
    - match (re.Match): A regular expression match object.

    Returns:
    - str: The swapped punctuation mark.
    """
    if match.group(1):  # If '.' is matched
        return '?'
    elif match.group(2):  # If '?' is matched
        return '.'
    else:  # If both '.' and '?' are matched
        char = match.group(0)
        if char == '.':
            return '?'
        elif char == '?':
            return '.'
        
def return_generic_response(responses, message):
    """
    Return a generic response based on the user's message.

    Args:
    - message (str): The user's input message.

    Returns:
    - str: A generic response based on the message.
    """    
    if message.upper().startswith('HELLO') or message.upper().startswith('HI'):
        return 'Hello!! :-)'

    if message.upper().startswith('OK'):
        return 'Great!'

    if 'YES' in message.upper() or 'NO' in message.upper():
        return 'Ok'
    
    return random.choice(responses).capitalize()