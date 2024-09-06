import numpy as np
import matplotlib.pyplot as plt #Matplotlib’s Pyplot module, used for creating plots and visualizations.
import string
import math #basic math library
import request 

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

def check_breach_password(passwor):
    #this function is used to check if the password has been exposed in a breach
    S_Hash_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    #hashlib.sha1(...) is an algroithm used to convert to byte encoded
    #it will put it into "hash".

    #encode.(...) convert string into bytes
        


print("yay! code runs")
