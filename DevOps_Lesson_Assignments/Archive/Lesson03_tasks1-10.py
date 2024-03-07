from my_functions import get_integer_input, checkpoint

print("Task 1. Write the following code: a = 1/0;\n"
      "Task 2. Build a corresponding try-except block to avoid exception.")
var1 = get_integer_input("to do the division (ideally - zero, to show error catching)")

try:
    a = 1/var1
except ZeroDivisionError:
    print("We have caught a 'ZeroDivisionError' error: you have tried to divide by zero.")
else:
    print(f'The result of the division is: 1/{var1} = {1/var1}')
finally:
    print("This is the end of Task 1/2\n")

print("3. Is the following code legal?\n"
      "try:\n"
      "    x = 1\n"
      "finally:\n"
      "    print('finally')\n"
      "Yes. it is.")
checkpoint("run this code")
try:
    x = 1
finally:
    print("The latest 'finally' block is executed always,"
          " regardless of any previous behaviors\n")


print("Task 4. What exception types can be caught by the following handler?\n"
      "'Except:'")
checkpoint("to see my answer")
print("From what I have googled, it will catch all built-in exceptions:"
      "https://docs.python.org/3/library/exceptions.html#exception-hierarchy,\n"
      "as well as custom exceptions declared as subclasses of the built-in ones.\n"
      "What it will not catch are the syntax errors, which would actually prevent\n"
      "the code from execution, and python would not guess what exactly the\n"
      "developer 'meant here' ")
checkpoint("check Task 5")

print("\nTask 5. What is wrong with using the above type of exception handler?")
print("It will catch too many error/exceptions making debussing a long, \n"
      "troublesome and time-inefficient process.")
checkpoint("check Task 6")

print("\n6. What exceptions can be caught by the following handlers?"
      "(a) ..."
      "except IOError ...")
print("The 'IOerror' is an exception specific to input and/or output functions. "
      "In a system-related function such as open() or read(), any obstacles "
      "that prevent communication between your code and your computer system "
      "will be exhibited as a raised io error or similar exception. Similar "
      "exceptions might stem from io error itself, given that it has "
      "subclasses such as the FileNotFoundError.")
checkpoint("to check the rest of the answer")
print("\n(b)..."
      "except ZeroDivisionError ...")
print("A ZeroDivisionError in Python occurs when we try to divide a number by 0. "
      "We can’t divide a number by 0 otherwise it will raise an error.")
checkpoint("check Task 7-9.")

print("\n7. Create a text file named “words.txt” programmatically")
my_file = open("words.txt", "w+")
str7 = my_file.read()
print(f"The content of the file so far is: \n'{str7}'\n")
checkpoint("add my name into the file")

print("8. Write your name into the file")
my_file = open("words.txt", "w")
my_file.write("Edward12")
my_file.close()

print("9. Read your file content and print it")
my_file = open("words.txt", "r")
str9 = my_file.read()
print(f"The content of the file now is: \n'{str9}'\n")
my_file.close()
checkpoint("check Task 10.")

print("10. Write Hebrew content into your text file and print its content programmatically.")
# creating a file
my_file10 = open("hebrew.txt", "w", encoding='utf-8')
my_file10.write("")
my_file10.close()

# reading a file to show it is empty so far
my_file10 = open("hebrew.txt", "r")
str10 = my_file10.read()
print(f"The content of the file so far is: \n'{str10}'\n")
my_file10.close()

my_file10 = open("hebrew.txt", "w", encoding='utf-8')
my_file10.write("שלום! שמי אדוארד.")
my_file10.close()

my_file10 = open("hebrew.txt", "r", encoding='utf-8')
str11 = my_file10.read()
print(str11)
print("The content of the file is: ", str11)
my_file10.close()
