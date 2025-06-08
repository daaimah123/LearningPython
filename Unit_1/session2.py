# =======================================
#           Problem Set Version 1
# =======================================

# ~~~~~~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~
# Write a function print_list() that takes in a list lst as a parameter and prints out each item in the list.

def print_list(lst):
    for i in lst:
        print(i)

# print_list(["squirtle", "gengar", "charizard", "pikachu"])

# ~~~~~~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~
# Write a function doubled() that takes in a list of integers lst as a parameter and prints each item in the list multiplied by two.

def doubled(lst):
    new_list = []
    for i in lst:
        double = i*2
        print(double)

# doubled([1,2,3])
# ~~~~~~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~
# Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.
        new_list.append(double)
    print(new_list)
# doubled([1,2,3])

# ~~~~~~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~
# Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.

def flip_sign(lst):
    new_list = []
    for i in lst:
        multiplied = i * -1
        new_list.append(multiplied)
    return new_list

# print(flip_sign([1,-2,-3,4]))
# ~~~~~~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~
# Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.

def max_difference(lst):
    # sort
    lst.sort()
    # first index
    min = lst[0]
    # last index
    max = lst[len(lst) - 1]
    # largest - smallest
    return max - min
    
# print(max_difference([5,22,8,10,2]))
# ~~~~~~~~~~~~~~ Problem 6 ~~~~~~~~~~~~~~
# Write a function count_less_than() that takes in a list of integers 'numbers' and an 'integer' threshold as parameters and returns the number of items in numbers that are less than threshold.

def count_less_than(numbers, threshold):
    # threshold is a integer
    # numbers is a list
    # return # in numbers < threshold value
    # initialize counter at zero
    # iterate over list indeces
    # if element is < threshold than increment count by 1
    less_than_count = 0
    for i in numbers:
        if i < threshold:
            less_than_count += 1
    return less_than_count
    
# print(count_less_than([12,8,2,4,4,10], 5))

# ~~~~~~~~~~~~~~ Problem 7 ~~~~~~~~~~~~~~
# Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.

def get_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

# print(get_evens([1,2,3,4]))
# ~~~~~~~~~~~~~~ Problem 8 ~~~~~~~~~~~~~~
# Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).

def multiples_of_five():
    range_nums = range(1, 101) # need to use this syntax in emurable
    for num in range_nums:
        if num % 5 == 0:
            print(num)

# multiples_of_five()
# ~~~~~~~~~~~~~~ Problem 9 ~~~~~~~~~~~~~~
# Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.

def find_divisors(n):
    # given a integer ==> find divisor of that integer
    # find n range #'s inclusive of n
    
    new_list = [] 
    range_nums = range(1, n + 1)
    for i in range_nums:
        if n % i == 0:
            new_list.append(i)
    return new_list
        

# print(find_divisors(6))
# ~~~~~~~~~~~~~~ Problem 10 ~~~~~~~~~~~~~~
# Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# fizzbuzz(13)

# ~~~~~~~~~~~~~~ Problem 11 ~~~~~~~~~~~~~~
# Write a function print_indices() that takes in an integer list lst as a parameter and prints out the index of each item in the given list.
# Use the function range() to loop through the list indices.

def print_indices(lst):
    for i in range(len(lst)):
        print(i)

# print_indices([5,1,3,8,2])

# ~~~~~~~~~~~~~~ Problem 12 ~~~~~~~~~~~~~~
# Write a function linear_search() that takes in a list lst and value target as parameters. The function returns the index of target in lst if found. If target is not found in lst, return -1.

def linear_search(lst, target):
    new_list = []
    for index, element in enumerate(lst):
        if element == target:
            new_list.append(index)
    return new_list


# print(linear_search([1,4,5,2,8,5], 5))

# =======================================
#           Problem Set Version 2
# =======================================

# ~~~~~~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~
# Write a function convertTemp() that takes in celsius as a parameter, which denotes the temperature in celsius. The variable is a non-negative floating point number rounded to two decimal places. In the function, convert celsius into Kelvin and Fahrenheit and return the list ans, in which ans = [kelvin, fahrenheit].

# Note that:

# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00

# def convertTemp(celsius):
#     pass

# ~~~~~~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~
# Write a function average() that takes in a list of integers scores as a parameter and returns the average score.

# def average(scores):
#     pass

# ~~~~~~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~
# Write a function increment_values() that takes in a list of integers lst as a parameter and returns a new list containing each element incremented by 1.

# def increment_values(lst):
#     pass

# ~~~~~~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~
# Write a function check_num() that takes in a list of integers lst and an integer num as parameters and returns True if num is a value in lst and False otherwise.

# def check_num(lst, num):
#     pass

# ~~~~~~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~
# Write a function find_missing() that takes in a list nums containing n unique numbers in the range [0,n]. The function returns the only number in the range that is missing from the list.

# def find_missing(nums):
#     pass

# ~~~~~~~~~~~~~~ Problem 6 ~~~~~~~~~~~~~~
# Write a function reverse_list() that takes in a list lst as a parameter and returns a new list containing the elements of lst in reverse order.

# def reverse_list(lst):
#     pass

# ~~~~~~~~~~~~~~ Problem 7 ~~~~~~~~~~~~~~
# Write a function get_odds() that takes in a list of integers nums and returns a list of all odd numbers in nums.

# def get_odds(nums):
#     pass

# ~~~~~~~~~~~~~~ Problem 8 ~~~~~~~~~~~~~~
# Write a function multiplication_table() that takes in an integer num and prints the multiples of that integer from 1 to 10.

# def multiplication_table(num):
#     pass

# ~~~~~~~~~~~~~~ Problem 9 ~~~~~~~~~~~~~~
# Write a function list_to_number() that takes in a list digits where each item is a digit between 0-9. The function returns the number they represent when combined.

# def list_to_number(digits):
#     pass

# ~~~~~~~~~~~~~~ Problem 10 ~~~~~~~~~~~~~~
# Write a function move_zeroes() that takes in an integer list nums and returns a new list with all the 0 values moved to the end of the list. The relative non-zero elements in the original list should be maintained.

# def move_zeroes(nums):
#     pass

# ~~~~~~~~~~~~~~ Problem 11 ~~~~~~~~~~~~~~
# Write a function print_odd_indices() that takes in a list nums as a parameter and prints out items at odd indices in the list.

# def print_odd_indices(nums):
#     pass

# ~~~~~~~~~~~~~~ Problem 12 ~~~~~~~~~~~~~~
# Write a function find_all_occurrences() that takes in a list lst and a value target as parameters and returns a list of all indices where target is found in lst.

# def find_all_occurrences(lst, target):
#     pass