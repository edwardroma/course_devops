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

# Challenges
print("\033[1mChallenges:\033[0m\n")
# M.
print("\033[1mTASK M.\033[0m Create a nested for loop (loop inside another loop) to create a pyramid shape:")
print("I need a number of lines.")
n = ich()
br(f"draw a pyramid {n} lines high and {n} characters wide")
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print("*"*j, end="")
    print()
br("check Task N")

print("\n\033[1mTASK N.\033[0m Create a nested for loop to create X shape "
      "(width is 7, length is 7):")
print("I need a square size (ideally - of 7) to fit the cross in.")
n = 1 + ich()
for i in range(1, n):
    for j in range(1, n):
        if i == j or i + j == n:
            print("x", end="")
        else:
            print(" ", end="")
    print()
br("check task O")


print("\n\033[1mTASK O.\033[0m Write a program with the following:")
print("\033[1mPart 1.\033[0m Function that gets a number from the user (using input).")


def get_num():
    print("Please give me some number. ")
    xx = ich()
    return xx


gn = get_num()
print(f"We have received from the user: {gn}")

br("do part 2")
print("\033[1mPart 2.\033[0m Function that receive the number from the first method, "
      "and computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)")


def int_sum(inin):
    sum1 = 0
    mx = len(str(inin))
    inst = str(inin)
    print(f"As a result, the number from the Task 1: '{inin}' is equal to ", end="")
    for ii in range(mx):
        sum1 = sum1 + int(inst[ii])
        if ii + 1 != mx:
            print(f'{inst[ii]} + ', end="")
        else:
            print(f'{inst[ii]} = ', end="")
    print(f"{sum1}")


int_sum(gn)

br("check task P")

print("\n\033[1mTASK P. Write a Python program to convert the below tuple to a string:\033[0m")
tup = ('h', 'e', 'l', 'l', 'o')
print("This is the tuple we are given: ", tup)


def tup_to_str(tp):
    lst1 = ""
    for ii in tp:
        lst1 = lst1 + str(ii)
    return lst1


br("run 'tup_to_str()' function")
str1 = tup_to_str(tup)
print("The result is: ", str1, type(str1))
br("check task Q")

print("\n\033[1mTASK Q: Write a Python program to get the smallest number from a list.\033[0m")
list1 = [55, 34, 9, 123, 345, 9, 738]
print(f'This is my original list: {list1}')
br("define the smallest number")
while len(list1) > 1:
    if list1[0] > list1[1]:
        list1.pop(0)
    else:
        list1.pop(1)
print(f'This is my list\'s smallest value: {list1[0]}')

print("\033[1mThat's it. Thanks for checking.\033[0m Your feedback is highly appreciated."
      " As much as more challenges :) )")
