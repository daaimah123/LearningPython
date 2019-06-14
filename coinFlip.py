from random import random

def coinFlip():
    # generate random number 0 - 1
    if random() > 0.5: 
        return "heads"
    else:
        return "tails"
print(coinFlip())