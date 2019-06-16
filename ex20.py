from sys import argv

# giving arguments (name of current file and file to be read) to the file from terminal
# terminal command ==> python3 ex20.py aint_i_a_woman.txt
script, input_file = argv

# defining a function to read and print the entire file contents
def print_all(f):
    print(f.read())

# a file to rewind file to beginning of file at character 0
def rewind(f):
    f.seek(0)

# defining a function that takes the file and prints out specific line contents and line number, with .strip() removing any trailing or leading whitespace
def print_a_line(f):
    with open(input_file) as f:  
        line = f.readline()
        count = 1
        while line:
            print(f"Line {count}: {line.strip()}")
            line = f.readline()
            count += 1

current_file = open(input_file)
print('First let\'s print the whole file:\n')

print_all(current_file)
print('Now let\'s rewind like a tape')

print_all(current_file)
print('Let\'s print three lines:')

# print out incremented line number and associate line contents
print_a_line(input_file)
