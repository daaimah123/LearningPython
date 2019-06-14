from pyfiglet import figlet_format
from termcolor import colored
from random import choice

def print_word_art(message, color):
    termcolors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan')
    if color not in termcolors: 
        color = choice(termcolors)
    art = figlet_format(message, font='slant')
    coloredArt = colored(art, color=color)
    print(coloredArt)

print('What message do you want to print?')
message = input()
print('What color?')
color = input()

print_word_art(message, color)