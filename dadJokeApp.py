from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import choice

url = 'https://icanhazdadjoke.com/search'

# game title art
def heading_art(message):
    heading = figlet_format(message, font='standard')
    colored_heading = colored(heading, color='blue')
    print(colored_heading)
heading_art('Dad Joke Game!')

# game prompt
joke_search_prompt = input('Let me tell you a joke! Give me a topic: ')
res = requests.get(url, headers={'Accept': 'application/json'}, params={'term': joke_search_prompt}).json()
results = res['results']

# length of results
num_jokes = res['total_jokes']
# handling joke output
def dad_jokes(num_jokes):
    if num_jokes > 1:
        random_joke = choice(results)['joke']
        print(f'''Wow, this query has {num_jokes} jokes! Here is one: 
        {random_joke}''')
    elif num_jokes == 1:
        single_joke = results[0]['joke']
        print(f'There is 1 joke. Take a look: "{single_joke}"')
    else: 
        print('''I am sorry, try another search term, 
        I have no jokes for that entry.''')
dad_jokes(num_jokes)