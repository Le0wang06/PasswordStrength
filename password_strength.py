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

