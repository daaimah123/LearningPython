from sys import argv

script, blah, blahblah, blahblahblah = argv

prompt = '>>>'

print('Script Name:', script)
print('What is your name? ')
name = input(prompt)
print('First:', blah)
print(f'Nice to meet you {name}. How old are you? ')
input(prompt)
print('Second:', blahblah)
print('Third:', blahblahblah)