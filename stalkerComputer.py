from sys import argv

script, user_name, user_fav_color = argv
prompt ='>'

print(f'Hi {user_name}, I\'m the {script} script!')
print(f'Do you like me {user_name}?')
likes = input(prompt)

print('Where do you live?')
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print(f'''I see your you like {user_fav_color}! 
    That\'s my favorite color too! 
    Let\'s be best friends! 
    What do you say?''')
best_friends = input('(Y/N)  ').lower()

def besties(best_friends):
    if best_friends == 'y' or best_friends == 'yes':
        print('OMG I can\'t believe it! We are going to have so much fun together!😏 BFFs')
    else:
        print("Okay, I understand...😭 I don't need any besties...") 

print(f'''
    You said {likes} about liking me. 
    You live in {lives}. 
    And you have a {computer} computer.
    Is this correct?
    ''')
correct = input('(Y/N)  ').lower()

def capture_correct(correct):
    if correct == 'y' or correct == 'yes':
        print('Wonderful! I got all your information correct!')
    else:
        print("Sorry about that! I will capture your information accurately next time.") 

besties(best_friends)
capture_correct(correct)