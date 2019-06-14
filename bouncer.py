# exploring conditionals

# ask for age
print('How old are you?')
age = input()
if age != '':
    if int(age) >= 21:
        print('normal entry')
    elif int(age) >= 18 and int(age) < 21:
        print('you get a wristband')
    else: 
        print('you\'re too young, sorry')
else: 
    print('please enter a string')
#18-21 wristbanch
#21+ drink, normal entry
#too young, sorry