# This is a function for task breaking, for the sake of readability
def br(act):
    input(f'Press \'Enter\' to {act}: ')


# This is the function to nake sure that the input is an integer.
def ich():
    while True:
        m = ""
        try:
            m = input("Please type in an integer: ")
            nn = int(m)
            break
        except ValueError:
            print(f"Your input '{m}' does look like an integer. Let's try again...")
    return nn


# Disclaimer
print("\033[1mDISCLAIMER:\033[0m To keep more focused on non-trivial tasks, "
      "\nI am not including the error-proof's everywhere. \nSo please try and "
      "use only the valid data types.\n")


# G.
print("\n\033[1mG. Write a program with the following: \033[0m")
print("\033[1mPart 1.\033[0m Function named 'printhello()' that prints the word “hello”.")


def printhello():
    print("hello")


br("run 'printhello()' function")
printhello()

print("\033[1mPart 2.\033[0m Function named calculate() which adds 5+3.2 and prints the result.")


def calculate():
    print(5+3.2)


br("calculate the sum. It is")
calculate()

print("\033[1mPart 2a.\033[0m Function named calculate2() whill ask you for 2 numbers print the sum result.")


def calculate2():
    print("Give me the 1st number. ", end="")
    xx = ich()
    print("Give me the 2nd number. ", end="")
    yy = ich()
    print(f'The sum is: ', xx + yy)


br("calculate the sum")
calculate2()
br("check task H")

# H.
print("\n\033[1mH. Write a program with the following:\033[0m")
print("\033[1mPart 1.\033[0m Function that receives a name as an argument and prints it.")


def print_name(name):
    print(name)


name1 = input("Give me your name, please: ")
print_name(f'Your name is {name1}')
br("proceed to part 2")

print("\033[1mPart 2.\033[0m Function that receive a number, divide it by 2, and prints the result.")


def div():
    while True:
        try:
            num = float(input("Give me the float number: "))
            print(f'Your final number is {num/2}')
            break
        except ValueError:
            continue


div()

br("check Task I")

# I.
print("\n\033[1mTASK I. Write a program with the following:\033[0m")
print("\033[1mPart 1.\033[0m Function that receive two numbers, add them, and return the sum.")


def num_sum(val1, val2):
    print(val1 + val2)
    return val1 + val2


print("This will be value 1: ")
value1 = ich()
print("And this will be value 2: ")
value2 = ich()


print(f'So your two numbers are: {value1} and {value2}. And their sum is:')
num_sum(value1, value2)
br("go to part 2")


print("\n\033[1mPart 2.\033[0m Function that receive two Strings, "
      "add space between them, and return one spaced string.")
print("\033[1mSolution 1.\033[0m The two Strings have been predefine by the developer. "
      "They are: \'44\' and \'33\':")


def str_sum1(str_value1, str_value11):
    str_res1 = str(str_value1) + " " + str(str_value11)
    return str_res1


res = str_sum1(44, 33)
print(f"This is our result: '{res}'")


print("\n\033[1mSolution 2.\033[0m The user defines the initial strings:")


def str_sum2():
    str_value2 = input("Please give me your first string: ")
    str_value22 = input("Please give me your second string: ")
    str_res2 = str_value2 + " " + str_value22
    print("This is your result:", str_res2)


str_sum2()

# J.
print("\n\033[1mTASK J. Create a program with the following:\033[0m")
print("\033[1mPart 1.\033[0m Create a list with 3 numbers")
print("\033[1mSolution 1a\033[0m")
br("autogenerate the list")
lst = []
for n in range(3):
    lst.append(n)
print("Our auto-list is: ", lst)

print("\n\033[1mSolution 1b.\033[0m")
br("generate the list manually")
list1: list[str] = []
while len(list1) < 3:
    list1.append(input("Give me an input to make a list: "))
print("Our 'manual' list is: ", list1)

print("\n\033[1mPart 2.\033[0m Iterate through the list to print all elements.")
br("count using 'for'")
for i in lst:
    print(f'item # {lst.index(i) + 1} is {i}')

br("count using 'while'")
count = 0
while count < 3:
    print(f"Elvis counts {count+1} for '{lst[count]}'")
    count += 1
print("Task completed.")
br("check Task K")

# K.
print("\n\033[1mK. Create a program which will get a list of numbers and "
      "prints the sum of all items.\033[0m")
lst = list((1, 2, 44, 55, 73, 23, 23, 22))
print("The pre-defined list is ", lst)


def pr(listing):
    kk = 0
    count1 = 1
    for ii in listing:
        print(f'Item # {count1} is: ', ii)
        kk = kk + ii
        print(f'The sum for {count1} elements is: ', kk)
        count1 += 1
    print(f'The total sum is: ', kk)


pr(lst)

print("Task K is done.")
br("check task L")

# L.
print("\033[1mTASK L.\033[0m Write a Python program to iterate over dictionaries and prints all keys using for loop.")
br("create a dictionary manually")
dict1 = {}
x: int = 1
y: str = "1"
while x != "":
    try:
        x = int(input("Enter a key:"))
        if x == "":
            break
        else:
            y = input("Enter a value:")
            dict1.update({x: y})
    except ValueError:
        print("Not an integer")
else:
    pass
print(f'As a result we have the following dictionary: {dict1}')

br("print all keys using 'for loop")


def prnt_keys(dct):
    count1 = 1
    keys = list()
    for ii in dct:
        print(f"Key # {count1} is: ", [ii])
        keys.append(ii)
        count1 += 1
    print("Catching the keys inside the function: ", keys)
    return keys


list_keys: list[str] = prnt_keys(dict1)
print("Printing the same from the variable stored outside the function:", list_keys)

print("Here are our keys: ", prnt_keys(dict1))

br("move on to Challenges")
exec(open("Lesson02_M_to_Q.py").read())
