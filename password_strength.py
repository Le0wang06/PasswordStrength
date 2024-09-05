import numpy as np # https://numpy.org/doc/2.1/user/basics.html
import matplotlib.pyplot as plt #Matplotlib’s Pyplot module, used for creating plots and visualizations.
import string
import math #basic math library

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



print("yay! code runs")
