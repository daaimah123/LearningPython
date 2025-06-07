def hello_world():
    print("Hello world!")

# hello_world()


def todays_mood():
    mood = "🙂"
    print("Today's mood: " + mood)

# todays_mood()


def print_menu(menu):
    print("Lunch today is: " + menu)

# print_menu("🌮")

def sum(a, b):
    sum = a + b
    doubleSum = 2 * sum
    return doubleSum

# print(sum(1, 2))

def product(c, d):
    productNums = c * d
    return productNums

# print(product(2, 4))

def classify_age(age):
    if age < 18 and age > 1:
        return 'child'
    elif age >= 18:
        return 'adult'
    else:
        return 'not greater than 1'

# print(classify_age(7))
# print(classify_age(-7))

def what_time_is_it(hour):
    # If hour is 2, the function should return "taco time 🌮".
    if hour == 2:
        return "taco time 🌮"
    # If hour is 12, the function should return "peanut butter jelly time 🥪”.
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    # Otherwise, the function should return "nap time 😴".
    else:
        return "nap time 😴"
    
# print(what_time_is_it(2))
# print(what_time_is_it(12))
# print(what_time_is_it(5))


def blackjack(score):
    # If score equals 21, print "Blackjack!".
    if score == 21:
        print("Blackjack!")
    # If score is greater than 21, print "Bust!".
    if score > 21:
        print("Bust!")
    # If score is greater than or equal to 17 and less than 21, print "Nice hand!".
    if score >= 17 and score < 21:
        print("Nice hand!")
    # If score is less than 17, print "Hit me!".
    if score < 17:
        print("Hit me!")

# blackjack(24)
# blackjack(19)
# blackjack(21)
# blackjack(10)

def get_first(lst):
    # if empty return None
    if len(lst) == 0:
        return None
    # find first item in a list and return the item
    else:
        return lst[0]

# print(get_first([1, 2, 3])) # 1
# print(get_first([])) # None

def get_last(lst):
    # if empty return None
    if len(lst) == 0:
        return None
    # find last item in a list and return the item
    else:
        return lst[0]

# print(get_last([1, 2, 3])) # 1
# print(get_last([])) # None