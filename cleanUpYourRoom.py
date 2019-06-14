print('Parent: How many times do I have to tell you to clean your room? ')
askTimes = input('Child Response: ')
askTimes = int(askTimes)

for time in range(askTimes):
    print('Clean Your Room')
    if time >=3:
        print("Listen to my words.")
        break