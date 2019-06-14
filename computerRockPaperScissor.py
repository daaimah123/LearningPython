# single user and computer game with conditional and input

import random
player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:    
    randomNum = random.randint(1, 3)
    if randomNum == 1:
        computer = 'rock'
    elif randomNum == 2:
        computer = 'paper'
    else:
        computer = 'scissors'

    print("...rock...")
    print("...paper...")
    print("...scissors...")

    print('Enter your choice')
    You = input()
    # print(f'Player Choice: {You}')
    # print(f'Computer Choice: {computer}')
    if You == 'quit' or You == 'q':
        break
    elif (You == 'rock' or You == 'paper' or You == 'scissors') and (computer == 'rock' or computer == 'paper' or computer =='scissors'):
        if You == 'rock':
            if computer == "paper":
                print('You: ' + You + ', Computer: ' +  computer + '. Computer wins')
                computer_wins += 1
            elif computer == "scissors":
                print('You: ' + You + ', Computer: ' +  computer + '. You win')
                player_wins += 1
            else:
                print('You are tied!')
        elif You == 'scissors':
            if computer == "rock":
                print('You: ' + You + ', Computer: ' +  computer + '. Computer wins')
                computer_wins += 1
            elif computer == "paper":
                print('You: ' + You + ', Computer: ' +  computer + '. You win')
                player_wins += 1
            else:
                print('You are tied!')
        elif You == 'paper':
            if computer == "scissors":
                print('You: ' + You + ', Computer: ' +  computer + '. Computer wins')
                computer_wins += 1
            elif computer == "rock":
                print('You: ' + You + ', Computer: ' +  computer + '. You win')
                player_wins += 1
            else:
                print('You are tied!')
        print(f'Player Score: {player_wins}, Computer Score: {computer_wins}')
    else:
        print('You did not entered rock, paper, or scissors.')
# print(f'Thanks for playing! Final Score: Player - {player_wins}, Computer- {computer_wins}')
if player_wins > computer_wins:
    print('Congrats You Won!')
elif player_wins == computer_wins: 
    print('You Are Tied!')
else: 
    print('The Computer Beat You!')