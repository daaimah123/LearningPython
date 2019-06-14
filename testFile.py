from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying {from_file} to {to_file}.')
# get contents of from_file
from_file_contents = open(from_file).read()
# from_file length in bytes
from_file_bytes = len(from_file_contents)
print(f'{from_file} is {from_file_bytes} bytes long')

# check the contents of to_file before add
prev_to_file_contents = open(to_file).read()
print(f'''This is what {to_file} looks like before adding to it:
    {prev_to_file_contents}
    ''')
# to_file length in bytes before
prev_to_file_bytes = len(prev_to_file_contents)
print(f'{to_file} is {prev_to_file_bytes} bytes long before adding')

print(f'Does to file exist? {exists(to_file)}')
# write from_file into to_file
write_in_to_file = open(to_file, 'w').write(from_file_contents)

# check the contents of to_file after add
after_to_file_contents = open(to_file).read()
print(f'''This is what {to_file} looks like after adding to it:
    {after_to_file_contents}
    ''')
# to_file length in bytes after
after_to_file_bytes = len(after_to_file_contents)
print(f'{to_file} is {after_to_file_bytes} bytes long after adding')
