# This is a function for task breaking, for the sake of readability
def br(act):
    input(f'Press \'Enter\' to {act}: ')


# This is the function to nake sure that the input is an integer.
def ich() -> int:
    m: int = 1
    while True:
        try:
            m = int(input("Please type in an integer: "))
            break
        except ValueError:
            print(f"Your input '{m}' does look like an integer. Let's try again...")
    return m


# Disclaimer
print("\033[1mDISCLAIMER:\033[0m To keep more focused on non-trivial tasks, "
      "\nI am not including the error-proof's everywhere. \nSo please try and "
      "use only the valid data types.\n")

# A.
print("\033[1mTASK A. 1 Create two numeric variables and compare them.\033[0m")
print("IMPORTANT! Equal valid entries will end the task.")
br("start")

X = 1
Y = 2
while X != Y:
    X = ich()
    Y = ich()
    if X > Y:
        print("BIG")
    elif X < Y:
        print("small")
    else:
        print("The task ends here: Both your entries are equal and the same.)")
br("go and check Task B")

# B.
print("\n\033[1mTASK B: Run a “for” loop 5 times and print the iteration number every time.\033[0m")
print("\033[1mSolution 1:\033[0m Insert \"if\" into the \"for\" loop.")
list1 = [1, 6, 3, 0, 5, 6, 9, 8, 9]
count = 0
print("I have this list manually created: ", list1)
br("run 5 cycles")
for value in list1:
    if count < 5:
        count += 1
        print(f'count {count} is {list1[value]}')
print("Solution 1 has been presented)")
br('check Solution 2')

print("\n\033[1mSolution 2:\033[0m Create a list of 5 elements and run for it the loop 5 times")
print("Creating a list...")
list2: list[int] = []
print(f'Right now my list \"{list2}\" contains {len(list2)} elements.')
print('Adding 5 items to it ...')

x = 0
while len(list2) < 5:
    list2.append(x)
    x += 1
print(f'Now I have a list {list2} that has {len(list2)} elements.')
br('do the counting')
count = 1
for item in list2:
    print(count)
    count += 1

# C.
print("\n\033[1mTASK C: Initialize a variable with a number 1-4, print a different season name for each number.\033[0m")
print("Please give me a number between 1 and 4 (inclusively). ", end="")
season = ich()
if season == 1:
    print('Your season is \"summer\"')
elif season == 2:
    print('Your season is \"winter\"')
elif season == 3:
    print('Your season is \"fall\"')
elif season == 4:
    print('Your season is \"spring\"')
else:
    print('You lost your chance! Re-study numbers and come again)')
br('check Task D')

# D.
print("\n\033[1mTASK D: How many times will the following loop run? What will be printed last?\033[0m")
my_guess = 10
print(f'My guess is {my_guess} - both times.')
br('check the correct answer')
count = 1
while count < 11:
    print(count)
    count = count + 1
count_d = count
print(f"So last digit is the same as the count number: {count_d}")
br('check Task E')

# E.
print("\n\033[1mTASK E: Write a program with variables holding your personal data.\033[0m")
print("Let's put in the following details:")
print("What is your age? ", end="")
age = ich()
letter = input("Please give me the 1st letter of your last name: ")
print("What is the current shekel/dollar rate? ", end="")
rate = ich()
abr1 = input("Have you ever flown abroad?  Please type in \"True\" or \"False\". : ")
if abr1 == "False":
    abr2 = False
elif abr1 == "True":
    abr2 = True
else:
    print("I'll take it for 'False'")
    abr2 = False
print("What is apartment number? ", end="")
ap_num = ich()
print("\033[1mThis is our summary:\033[0m")
print(f'My age is {age}. My letter is {letter}. The rate is {rate}.')
print(f'Have I flown abroad? {abr2}. My apartment number is {ap_num}')
print(f'Currency Rate + Age are either {rate + age} (numeric) or {str(rate)+str(age)} (literal)')
br("check Task F")

# F.
print("\n\033[1mTASK F. Create a program which asks the user for his phone number and prints it out.\033[0m")
print("Please give me your phone number: ")
tel_num = ich()
print(f'Your phone number is: {tel_num}')
br("check task G")

exec(open("Lesson02_G_to_L.py").read())
