# exploring multiple user game with input and conditionals

print("...rock...")
print("...paper...")
print("...scissors...")

print('Player 1 enter your choice')
player1 = input()
print('Player 2 enter your choice')
player2 = input()

if (player1 == 'rock' or player1 == 'paper' or player1 == 'scissors') and (player2 == 'rock' or player2 == 'paper' or player2 =='scissors'):
    if player1 == 'rock':
        if player2 == "paper":
            print('Player 1: ' + player1 + ', Player 2: ' +  player2 + '. Player 2 wins')
        elif player2 == "scissors":
            print('Player 1: ' + player1 + ', Player 2: ' +  player2 + '. Player 1 wins')
        else:
            print('You are tied!')
    elif player1 == 'scissors':
        if player2 == "rock":
            print('Player 1: ' + player1 + ', Player 2: ' +  player2 + '. Player 2 wins')
        elif player2 == "paper":
            print('Player 1: ' + player1 + ', Player 2: ' +  player2 + '. Player 1 wins')
        else:
            print('You are tied!')
    elif player1 == 'paper':
        if player2 == "scissors":
            print('Player 1: ' + player1 + ', Player 2: ' +  player2 + '. Player 2 wins')
        elif player2 == "rock":
            print('Player 1: ' + player1 + ', Player 2: ' +  player2 + '. Player 1 wins')
        else:
            print('You are tied!')
else:
    print('someone has not entered rock, paper, or scissors')