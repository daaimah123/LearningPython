# myName.txt (filename1)
# 1. My name is Daaimah Tibrey!
# 2. 
# 3.

# myFormerName.txt (filename2)
# 1. My previous name was Daaimah Brown.

# myName.py (filename3)
from sys import argv


# terminal command: python3 myName.py myName.txt myFormerName.txt 
filename3, filename1, filename2 = argv


# taking in given filename1 parameter from command line
print(f'Here is your {filename1} file!')
# telling computer to retrieve filename1 per given parameter name
open_file1 = open(filename1)
# read and print text from filename1
read_file = print('>>>>' + open_file1.read() + '<<<<')


# taking in given filename2 parameter from command line
print(f'Here\'s the second file name: {filename2}.')
# telling computer to retrieve filename2 per given parameter name
open_file2 = open(filename2)
# read and print text from filename2
read_file2 = print('>>>>' + open_file2.read() + '<<<<')

# NOTE: file output from text is carriage and space sensitive, 

# Notice that filename1 has two carriage returns in the file
# spanning line 2 and 3. As such it prints them to the terminal: 
# >>>>My name is Daaimah Tibrey!
#
#
# <<<<

# Meanwhile filename2, which does not have extra carriage returns
# prints out as:
# >>>>My previous name was Daaimah Brown.<<<< 


# Get text file lines directly from the python3 shell using the 'read' argument and 'readlines' function and : 
# >>> read = open('myName.txt', 'r')
# >>> read
# <_io.TextIOWrapper name='myName.txt' mode='r' encoding='UTF-8'>
# >>> read.readlines()
# ['My name is Daaimah Tibrey!\n', '\n']
# >>> read.close()
# Check it out! It even captured those carriage returns again!

# Even cooler stuff in the python3 shell!
# using file_name.truncate() will remove text from your file and print 0 characters
# in order to do this, you will need to use the write argument on the open function:
# >>> read = open('myName.txt', 'w')
# >>> read.truncate()
# 0
# if you want to add new text to the file, use the file_name.write() function:
# >>> read.write('New  text in myName.txt file \n My name is Daaimah Tibrey!')
# 57
# to see the changes you will have to close the file and reopen it to save
# changes and make them readable:
# >>> read.close()
# >>> read = open('myName.txt', 'r')
# >>> read.readlines()