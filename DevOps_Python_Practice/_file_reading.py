# ALL FILE MANIPULATIONS MUST BE DONE with the FILE not its NAME
# SO! OPEN() IT FIRST

# 1. Print the file NAME
file_name = "ttt.txt"
print("1. print file name - Just the file NAME:", file_name)
print()

# 2. Print the file DETAILS
file_opened = open(file_name, "r")
print("2. File DETAILS- print open(file, r)", file_opened)
print()

# 3. Print file CONTENT as a Tuple
file_opened_read_by_line = file_opened.readlines()
print("3. File CONTENT in one line - print file_opened.readlines()", file_opened_read_by_line)
print()

# 4. Print file CONTENT by line
file_opened = open("ttt.txt", "r")
print("4. File CONTENT 'by line' - file_opened.read\n", file_opened.read())


####################
# Reading a File
with open('example.txt', 'r') as file:
    content = file.read()
    print("Reading a File", content)

# Writing to a File
with open('example.txt', 'w') as file:
    file.write('Hello, Python!')

# Appending to a File
with open('example.txt', 'a') as file:
    file.write('\nAppend this line.')

# Reading Lines into a List
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("Reading Lines into a List", lines)

# Iterating Over Each Line in a File
with open('example.txt', 'r') as file:
    for line in file:
        print("Iterating Over Each Line in a File", line.strip())

# Checking If a File Exists
import os
if os.path.exists('example.txt'):
    print('File exists.')
else:
    print('File does not exist.')

# Writing Lists to a File
lines = ['First line', 'Second line', 'Third line']
with open('example.txt', 'w') as file:
    for line in lines:
        file.write(f'{line}\n')

# Using With Blocks for Multiple Files
# To work with multiple files simultaneously using with blocks:
with open('source.txt', 'r') as source, open('destination.txt', 'w') as destination:
    content = source.read()
    destination.write(content)

# Deleting a File
# To safely delete a file if it exists:
import os
if os.path.exists('example.txt'):
    os.remove('example.txt')
    print('File deleted.')
else:
    print('File does not exist.')

# Reading and Writing Binary Files - in binary mode (useful for images, videos, etc.):
# Reading a binary file
with open('image.jpg', 'rb') as file:
    content = file.read()
# Writing to a binary file
with open('copy.jpg', 'wb') as file:
    file.write(content)
    