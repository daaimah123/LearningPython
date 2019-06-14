import random

random_number = random.randint(1, 10)


#get user guess
guess = None

while random_number !=  guess:
    # ask for a new guess
    guess = input('Guess a Number 1 to 10:  ')
    guess = int(guess)
    #check if random number is higher or lower than guess
    if random_number > guess:
        print('You guessed too low')
    elif random_number < guess:
        print('You guessed too high')
    else: 
        print('You got it')
        play_again = input('Do you want to play again? (y/n)  ')
        if play_again == 'y':
            random_number = random.randint(1, 10)
            guess = None
        else:
            print('Thanks for playing')
            break
