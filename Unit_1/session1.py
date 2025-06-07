# run in terminal with python3 unit1.py

# =======================================
#  Problem Set Version 1 — All Complete
# =======================================


# ~~~~~~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~
# Given the following lines of code, work with your group members to place the lines in order and write and call your first Python function!

# a. print("Hello world!")
# b. def hello_world():
# c. hello_world()

def hello_world():
    print("Hello World! 🌎")

# hello_world()

# ~~~~~~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~
# The following function uses a variable, mood to print out "Today's mood: 😎". Copy this code to your Replit and update the mood variable to print out your mood for today.

# def todays_mood():
#     mood = "😎"
#     print("Today's mood: " + mood)

# todays_mood()

def todays_mood():
    mood = "🙃"
    print("Today's mood " + mood)

# todays_mood()

# ~~~~~~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~
# The following function accepts one parameter menu. Copy this code to your Replit and add a function call so that "Lunch today is: 🍕" is printed to the console.

# def print_menu(menu):
#     print("Lunch today is: " + menu)
def print_menu(menu):
    print('Lunch today is: '+ menu)

# print_menu('🍱')

# ~~~~~~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~
# The following function returns the sum of two integers: a and b.

# def sum(a, b):
#     return a + b
# Use the sum() function to calculate the sum of 13 and 27. Then, double the calculated sum and print the result to the console.
def sum(num1, num2):
    sum_of_nums = num1 + num2
    double = sum_of_nums * 2
    print(double)

# sum(3, 5)

# ~~~~~~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~
# Write a function product() that returns the product of two integers, a and b.

def product(int1, int2):
    product = int1 * int2
    return product

# print(product(4, 6))

# ~~~~~~~~~~~~~~ Problem 6 ~~~~~~~~~~~~~~
# Write a function classify_age() that takes an integer age as a parameter and returns "child" if the age is less than 18, and returns "adult" otherwise.
def classify_age1(age):
    if age < 18:
        return 'child'
    else:
        return 'adult'

# print(classify_age1(32))

def classify_age2(age):
    conditional = 'child' if age < 18 else 'adult'
    return conditional

# print(classify_age2(5))

# ~~~~~~~~~~~~~~ Problem 7 ~~~~~~~~~~~~~~
# Let's put what we learned in Problems 1-4 all together! Write a function named what_time_is_it() that takes an integer hour as a parameter.
# If hour is 2, the function should return "taco time 🌮".
# If hour is 12, the function should return "peanut butter jelly time 🥪”.
# Otherwise, the function should return "nap time 😴".
def what_time_is_it(hour):
    if hour == 2:
        return '🌮 taco time 🌮'
    elif hour == 12:
        return '🥪 peanut butter jelly time 🥪'
    else:
        return '🛌 nap time 🛌'

# print(what_time_is_it(15))

# ~~~~~~~~~~~~~~ Problem 8 ~~~~~~~~~~~~~~
# In the game Blackjack, players try to draw a hand of cards that totals as close to 21 as possible. Players "bust" if their cards total more than 21. Players say "Hit me!" if they want the dealer to give them another card.

# Write a function called blackjack() that takes an integer score as a parameter.
# If score equals 21, print "Blackjack!".
# If score is greater than 21, print "Bust!".
# If score is greater than or equal to 17 and less than 21, print "Nice hand!".
# If score is less than 17, print "Hit me!".
def blackjack(score):
    if score == 21:
        print('Blackjack!')
    elif score > 21:
        print('Bust!')
    elif score <= 17 and score < 21:
        print('Nice hand!')
    elif score > 17:
        print('Hit me!')

# blackjack(24)
# blackjack(19)
# blackjack(21)
# blackjack(10)

# ~~~~~~~~~~~~~~ Problem 9 ~~~~~~~~~~~~~~
# Write a function get_first() that takes in a list as a parameter and returns the first item in the list. Return None if the list is empty.

def get_first(list):
    return list[0] if len(list) > 0 else None

# print(get_first([3,1,6,7,5]))

# ~~~~~~~~~~~~~~ Problem 10 ~~~~~~~~~~~~~~
# Write a function get_last() that takes in a list as a parameter and returns the last item in the list. Return None if the list is empty.

def get_last(list):
    return list[len(list) - 1] if len(list) > 0 else None

# print(get_last([3,1,6,7,5]))

# ~~~~~~~~~~~~~~ Problem 11 ~~~~~~~~~~~~~~
# Write a function counter() that uses the range function to print numbers between 1 and a given stop value (inclusive).

def counter(stopNum):
    for i in range(1, stopNum):
        print(i)

# counter(7)
# ~~~~~~~~~~~~~~ Problem 12 ~~~~~~~~~~~~~~
# Write a function sum_ten() that returns the sum of numbers from 1 to 10.

def sum_ten():
    count = 0
    for num in range(1, 11):
        count += num
    return count

# print(sum_ten())

# ~~~~~~~~~~~~~~ Problem 13 ~~~~~~~~~~~~~~
# Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive).

def sum_positive_range(givenStop):
    count = 0
    for num in range(1, givenStop + 1):
        count += num
    return count

# print(sum_positive_range(6))

# ~~~~~~~~~~~~~~ Problem 14 ~~~~~~~~~~~~~~
# Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value (inclusive).

def sum_range(given_start, given_stop):
    count = 0
    for num in range(given_start, given_stop + 1):
        count += num
    return count

# print(sum_range(3, 9))

# ~~~~~~~~~~~~~~ Problem 15 ~~~~~~~~~~~~~~
# Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.

def print_negatives(lst):
    for i in lst:
        if i < 0: print(i)

# print_negatives([3,-2,2,1,-5]) 

# =======================================
#  Problem Set Version 2 — All Complete
# =======================================

# ~~~~~~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~
# Write a function greet_user() that takes in a string name as a parameter and prints "Hello <name>".

# def greet_user(name):
#     pass

# ~~~~~~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~
# Write a function difference() that returns the difference between two integers a and b (b should be subtracted from a).

# def difference(a, b):
#     pass

# ~~~~~~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~
# Given an integer list nums of length n, create a function concatenate_list() that creates and returns a list ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums lists.

# def concatenate_list(nums):
#     pass


# ~~~~~~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~
# Write a function sleep_assessment() that takes in an integer parameter hours indicating the number of hours the user slept.
# If hours is less than 8, print "Oof, go back to bed!".
# If hours is greater than or equal to 8 and less than or equal to 10, print "You got a good night's rest!".
# If hours is greater than 10, print "You're a sleep prodigy!".

# def sleep_assessment(hours):
#     pass

# ~~~~~~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~
# Write a function calculate_tip() that takes in a float bill and a string service_quality as parameters.
# If service_quality is "poor", the function should return 10% of the bill value.
# If service_quality is "average", the function should return 15% of the bill value.
# If service_quality is "excellent", the function should return 20% of the bill value.
# If service_quality is any other value, the function should return None.

# def calculate_tip(bill, service_quality):
#     pass

# ~~~~~~~~~~~~~~ Problem 6 ~~~~~~~~~~~~~~
# Write a function rock_paper_scissors() that determines the winner of a game of Rock, Paper, Scissors. The function accepts two strings as parameters: player1 and player2. Each parameter can have a value of "rock", "paper", or "scissors".

# Print either "Player 1 wins!" or "Player 2 wins!" according to the following rules:
# Rock wins against scissors.
# Scissors wins against paper.
# Paper wins against rock.

# If both player1 and player2 have the same value, print "It's a tie!".

# def rock_paper_scissors(player1, player2):
#     pass

# ~~~~~~~~~~~~~~ Problem 7 ~~~~~~~~~~~~~~
# Given the following lines of code, work with your group members to place the lines in order to write and call a function that divides each value in an input list by 2.

# a. result = []
# b. for number in lst:
# c. result.append(halved)
# d. halved = number/2
# e. halve_list([2,4,6,8])
# f. return result
# g. def halve_lst(lst):

# ~~~~~~~~~~~~~~ Problem 8 ~~~~~~~~~~~~~~
# Write a function above_threshold() that takes in a list of integers lst and an integer threshold as parameters. The function iterates through the original list and returns a new list containing only numbers that are greater than threshold.

# def above_threshold(lst, threshold):
#     pass

# ~~~~~~~~~~~~~~ Problem 9 ~~~~~~~~~~~~~~
# Write a function countdown() that takes in two positive integers m and n as parameters and prints numbers from m down to n.

# def countdown(m,n):
#     pass

# ~~~~~~~~~~~~~~ Problem 10 ~~~~~~~~~~~~~~
# Write a function power() that takes in two integers base and exponent. The function should return the value of the base number to the power of the exponent.

# def power(base, exponent):
#     pass

# ~~~~~~~~~~~~~~ Problem 11 ~~~~~~~~~~~~~~
# Without using the built-in len() function, write a function list_length() that takes in a list lst as a parameter and returns the length of the list.

# def list_length(lst):
#     pass

# ~~~~~~~~~~~~~~ Problem 12 ~~~~~~~~~~~~~~
# Write a function factorial() that takes in an integer n as a parameter and returns its factorial. The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 (denoted as 5!) is 5! = 5 * 4 * 3 * 2 * 1 which equals 120.

# def factorial(n):
#     pass

# ~~~~~~~~~~~~~~ Problem 13 ~~~~~~~~~~~~~~
# Write a function squares() that takes a list of integers nums as a parameter and returns a new list containing the square of each number in the original list.

# def squares(nums):
#     pass

# ~~~~~~~~~~~~~~ Problem 14 ~~~~~~~~~~~~~~
# Write a function multiply_list() that takes in a list of integers lst and an integer multiplier as parameters. The function returns a new list containing each value in lst multiplied by multiplier.

# def multiply_list(lst, multiplier):
#     pass

# ~~~~~~~~~~~~~~ Problem 15 ~~~~~~~~~~~~~~
# Write a function count_evens() that takes in a list of integers lst as a parameter. The function returns the number of even numbers in the list.

# def count_evens(lst):
#     pass

