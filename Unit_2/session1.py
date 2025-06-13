# =======================================
#          Problem Set Version 1
# =======================================
'''
~~~~~~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~
Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.

def is_subsequence(lst, sequence):
    pass

Example Usage:
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
Example Output: True
'''

'''
~~~~~~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~
Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.

def create_dictionary(keys, values):
    pass

Example Input:
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

Example Output:
{"peanut": "butter", "dragon": "fly", "star": "fish", "pop": "corn", "space": "ship"}
'''

'''
~~~~~~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~
Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. The function looks for the target and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".

def print_pair(dictionary, target):
    pass

Example Usage:
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

Example Output:
Key: patrick
Value: star
That pair does not exist!
Key: spongebob
Value: squarepants
'''

'''
~~~~~~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~
Write a function keys_v_values() that takes in a dictionary dictionary whose keys and values are both integers. The function should find the sum of all keys in the dictionary and the sum of all values.
If the sum of all keys is greater than the sum of all values, the function should return the string "keys".
If the sum of all values is greater than the sum of all keys, the function should return the string "values".
If keys and values have equal sums, the function should return the string "balanced".

def keys_v_values(dictionary):
    pass
Example Usage:

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
Example Output:

values
keys
💡 Hint: Accessing Keys, Values, and Key-Value Pairs
'''

'''
~~~~~~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~
Write a function restock_inventory() that updates an inventory dictionary based on a restock list. It accepts two parameters:

current_inventory: a dictionary where each key-value pair represents an item and its current stock in the inventory
restock_list: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory
If an item in restock_list is not present in the current_inventory, it should be added. The function should return the updated dictionary current_inventory.

def restock_inventory(current_inventory, restock_list):
    pass
Example Input:

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
Example Output:

current_inventory = {
    "apples": 40,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}
💡 Hint: Looping over Key-Value Pairs
'''


'''
~~~~~~~~~~~~~~ Problem 6 ~~~~~~~~~~~~~~
Write a function calculate_gpa() that calculates the grade point average (GPA) for a student based on their course grades and returns the gpa as a float. The function takes in a dictionary report_card as a parameter where each key-value pair represents a course and the grade received in that course respectively. The grades are represented as strings ("A", "B", "C", "D", "F") and each grade corresponds to a certain number of grade points:

"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

A GPA is calculated by finding the average of all grade points.

def calculate_gpa(report_card):
    pass

Example Usage:
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

Example Output: 3.33
'''


'''
~~~~~~~~~~~~~~ Problem 7 ~~~~~~~~~~~~~~
Imagine you are working on a book review software like Goodreads. Write a function named highest_rated() that returns the book with the highest rating.

The function should take in a list of dictionaries named books as a parameter. Each dictionary represents data associated with a book, including its title, author, and rating. The function should return the dictionary for the book with the highest rating.

def highest_rated(books):
    pass

Example Input:
books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

Expected Output:
{"title": "A Fortune For Your Disaster",
 "author": "Hanif Abdurraqib",
 "rating": 4.47
}
'''


'''
~~~~~~~~~~~~~~ Problem 8 ~~~~~~~~~~~~~~
Write a function index_to_value_map() that takes in a list lst and returns a dictionary that maps the index of each element in lst to its value.

def index_to_value_map(lst):
    pass

Example Input: lst = ["apple", "banana", "cherry"]
Example Output: {0: "apple", 1: "banana", 2: "cherry"}
'''

# =======================================
#          Problem Set Version 2
# =======================================

'''
~~~~~~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~
Write a function is_monotonic() that takes in a list nums as a parameter and checks if it is either monotone increasing or monotone decreasing.
A list is monotone increasing if every element is either greater than or equal to the element before it.
A list is monotone decreasing if every element is either less than or equal to the element before it.
The function should return True if the given list is either monotone increasing or decreasing and False otherwise.
Hint: This is a lists problem

def monotonic(nums):
    pass
Example Usage:

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))
Example Output:

True
True
True
False
'''

'''
~~~~~~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~
Write a function student_directory() that takes a list of student_names as a parameter and returns a dictionary of students, where each student in student_names is a key mapped to a unique numerical student ID.

def student_directory(student_names):
    pass
Example Input: student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
Example Output: {"Ada Lovelace": 1, "Tu Youyou": 2, "Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 5}
'''

'''
~~~~~~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~
The following function get_description() takes in a dictionary info and a list keys as parameters. For each key in keys, the function prints the value associated with that key in info and prints None if the key does not exist in info.

However, the function has a bug! Copy the function into your Replit and run the code. Work with your group members to find the cause of the bug and correctly implement the function.

def get_description(info, keys):
    for key in keys:
	    print(info[key])
   
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)
'''

'''
~~~~~~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~
Write a function sum_even_values() that returns the sum of all even values in a given dictionary. Assume the dictionary values are all integers.

def sum_even_values(dictionary):
    pass
Example Usage:

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))
Example Output: 14
'''

'''
~~~~~~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~
Write a function merge_catalogs() that combines two product catalogs, catalog1 and catalog2 as parameters. Each parameter is a dictionary where each key-value pair represents a product name and its price, respectively. If the same product exists in both catalogs, the price from the second catalog should overwrite the price in the first. Return the updated first catalog dictionary.

def merge_catalogs(catalog1, catalog2):
    pass
Example Input:

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
Example Output: {"apple": 1.0, "banana": 0.75, "cherry": 1.25}
'''


'''
~~~~~~~~~~~~~~ Problem 6 ~~~~~~~~~~~~~~
Write a function get_items_to_restock() that takes in a dictionary products that maps product names to their quantities and an integer restock_threshold as parameters. The function returns a list of products that have a value less than restock_threshold and need to be restocked. If products is empty, the function return an empty list.

def get_items_to_restock(products, restock_threshold):
    pass
Example Input:

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
Example Output: ["Product2", "Product4"]
'''


'''
~~~~~~~~~~~~~~ Problem 7 ~~~~~~~~~~~~~~
Imagine you're contributing to a move recommendation engine, and you're tasked with writing a function named most_popular_genre() that returns the genre with the highest average rating across all movies.

The function takes in a list of dictionaries named movies as a parameter. Each dictionary represents data associated with a movie, including its title, genre, and rating. The function calculates the average rating for each genre and returns the genre with the highest average rating.

def most_popular_genre(movies):
    pass
Example Usage:

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))
Example Output: Science Fiction
'''


'''
~~~~~~~~~~~~~~ Problem 8 ~~~~~~~~~~~~~~
Write a function quality_control() that takes in a dictionary product_scores and an integer threshold as parameters. The dictionary product_scores has key-value pairs that represent a product ID and its quality rating.
If the product has a score greater than or equal to threshold, the function categorizes it as a "pass".
If the product has a score less than threshold, the function categorizes it as a "fail".
The function returns a new dictionary where the key-value pair is the product ID and whether it is a "pass" or "fail".

def quality_control(product_scores, threshold):
    pass
Example Input:

scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold: 60
Example Output: {"x0123": "pass", "x0124": "fail", "x0125": "pass", "x0126": "fail"}
'''

# =======================================
#         Problem Set Version 3
# =======================================


'''
~~~~~~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~
A mountain list is defined as a list that has at least three elements, where there exists some i with 0 < i < len(lst)-1 such that lst[0] < lst[1] < ... lst[i-1] < lst[i] and lst[i] > lst[i+1] > ... > lst[len(lst)-1].

Given such a mountain list lst as a parameter, write a function that finds and returns the highest peak (the index i of the maximum element).

Hint: This is a lists problem

def peak_index_in_mountain_list(lst):
    pass
Example Usage:

mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)
Example Output: 2
'''


'''
~~~~~~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~
Write a function build_inventory() that takes in a list of product_names and a corresponding list of product_prices as parameters. The function returns a dictionary representing the inventory of a small store. Each product name in product_names should be a key in the dictionary and the corresponding value should be the item price.

product_names[i] should be paired with product_prices[i] in the dictionary where 0 <= i <= len(product_names). You may assume that product_names and product_prices are the same length.

def build_inventory(product_names, product_prices):
    pass
Example Input:

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
Example Output:

{
    "Apple": 0.99
    "Banana": 0.5
    "Orange": 0.75
}
'''


'''
~~~~~~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~
Write a function update_or_warn() that takes in a dictionary records, a key item, and a new value update_value as parameters. The function updates the value of item in records with update_value if item exists. If item does not exist, it should print "<item> not found!".

def update_or_warn(records, item, update_value):
    pass
Example Usage:

records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "banana", 5)

update_or_warn(records, "grape", 4)
Example Output:

# "banana" found, dictionary updated
# records = {"apple": 1, "banana": 5, "orange": 3}

Grape not found!
'''


'''
~~~~~~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~
Write a function attendance_rate() that takes in a dictionary attendance_list as a parameter. The function maps student names to their attendance status ("Present" or "Absent"), and returns the percentage of students who are present.

def attendance_rate(attendance_list):
	pass
Example Usage:

attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
}

print(attendance_rate(attendance_list))
Example Output: 50.0
'''


'''
~~~~~~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~
Write a function average_book_ratings(), that calculates the average rating for each book in a collection. The function takes one parameter: a dictionary book_ratings where each key-value pair represents a book title and a list of its ratings, respectively. Ratings are represented as floating-point numbers. The function should return a new dictionary with book titles as keys and their average rating.

def average_book_ratings(book_ratings):
    pass
Example Input:

book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
Example Output:

{
    "The Great Gatsby": 4.2,
    "To Kill a Mockingbird": 4.7
}
'''


'''
~~~~~~~~~~~~~~ Problem 6 ~~~~~~~~~~~~~~
Write a function odd_keys_even_values() that takes in dictionary as a parameter, a dictionary with integer keys and values. The function returns a list of keys that are odd where their corresponding values are even.

def odd_keys_even_values(dictionary):
    pass
Example Usage:

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)
Example Output:

[1, 5]
'''


'''
~~~~~~~~~~~~~~ Problem 7 ~~~~~~~~~~~~~~
You're developing an analytics tool for a sports league. Your task is to write a function named team_with_best_average_score() that returns the team with the highest average score over a season.

The function should accept a list of dictionaries named games as a parameter. Each dictionary represents data from a game, including the "team_name", and the "score" they achieved in that game. The function calculates the average score for each team across all games and returns the team with the highest average score.

def team_with_best_average_score(games):
    pass
Example Usage:

games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers", 
     "score": 30
    },
    {"team_name": "Lions", 
     "score": 27
    },
    {"team_name": "Bears", 
     "score": 20
    },
    {"team_name": "Tigers", 
     "score": 24
    },
    {"team_name": "Bears", 
     "score": 22
    }
]

print(team_with_best_average_score(games))
Example Output: Tigers
'''

'''
~~~~~~~~~~~~~~ Problem 8 ~~~~~~~~~~~~~~
Write a function find_unique_items() that takes two lists list_a and list_b as parameters. The function identifies unique items from the lists and returns a dictionary with the items as keys and a boolean value as the value indicating whether the item is unique to the first list (True) or not (False).

def find_unique_items(list_a, list_b):
    pass
Example Input:

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
Example Output: {"carrot": True, "date": False}
'''