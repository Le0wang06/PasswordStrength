import numpy as np
import matplotlib.pyplot as plt #Matplotlib’s Pyplot module, used for creating plots and visualizations.
import string

import math #basic math library

from flask import Flask, render_template, request
import requests # creates HTTP
import hashlib  # For creating the SHA-1 hash of the password

def calculate_entropy(password):
    length = len(password)
    if length == 0:
        return 0
    
    frequency = {}
    for char in password:
        frequency[char] = frequency.get(char,0) + 1
    
    entropy = 0
    for count in frequency.values():
        probability = count / length
        entropy -= probability * math.log2(probability)

    return entropy

def check_length(password):
    return len(password) >=8 

def check_complexity(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False 

    for each in password:
        if(has_special and has_lower and has_digit and has_upper):
            break
        if(each.isupper()):
            has_upper = True
        if(each.islower()):
            has_lower = True
        if(each.isdigit()):
            has_digit = True
        if each in string.punctuation:
            has_special = True

    return has_special and has_lower and has_digit and has_upper


def anaylyze_password(password):
    length_ok = check_length(password)
    entropy_ok = calculate_entropy(password)
    complexity_ok = check_complexity(password)
    result = ""

    if(length_ok and complexity_ok and entropy_ok > 3.0):
        result = "Strong"
    elif (length_ok and complexity_ok):
        result = "Moderate"
    else:
        result = "Weak"

    return result

def check_password_breach(password):
   
    # Turn password into hash
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #encode = convert into Byte

    # Only take the first 5 digit
    prefix = sha1_password[:5]
    
    # 
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    
    # (status code 200)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")
        #raise just bring up an exception

    # split text line by line
    hashes = (line.split(':') for line in response.text.splitlines())

    
    # loop 
    for suffix, count in hashes:
        if sha1_password[5:] == suffix:  # Compare the remaining part of the hash
            return True, int(count)  # Return True and the breach count if it was breached
    
    return False, 0

#THIS COULD BE USED TO CHECK YOUR CODE QUICKER USING CLI UI. DONT NEED TOOL OUTSIDE OF PYTHON

# def cli_ui():
#     print("Welcome to the Password Breach Checker!")
#     print("This tool checks if your password has been exposed in any known data breaches.")
    
#     while True:
#         password = input("Enter a password to check (or type 'exit' to quit): ")
        
#         if password.lower() == 'exit':
#             print("Exiting the Password Breach Checker. Stay safe!")
#             break
        
#         breached, count = check_password_breach(password)
        
#         if breached:
#             print(f"WARNING: Your password has been exposed {count} times in data breaches.")
#             print("It’s highly recommended to change this password immediately.")
#             print("Suggestions for a strong password:\n"
#                   "- Use at least 12 characters.\n"
#                   "- Include uppercase and lowercase letters, numbers, and symbols.\n"
#                   "- Avoid using common phrases or easily guessable words.")
#         else:
#             print("Good news! Your password has not been found in any known data breaches.")
#         print()  

# cli_ui()

app = Flask(__name__)
