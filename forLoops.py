# printing items of a string using a for loop

# for number in 'Daaimah':
#     print(number*50)


for x in range(1, 21):
    if x == 4 or x == 13:
        state = 'unlucky'
    elif x % 2 == 0:
        state = 'even'
    elif x % 2 != 0:
        state = 'odd'
    print(f'{x} is {state}')