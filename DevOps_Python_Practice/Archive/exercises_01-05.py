import datetime
import random
from my_functions import checkpoint, get_integer_input

# Exercise 1. Input amd print
name = input("gimme your name: ")
age = get_integer_input("to share your age: ")
curr_date = datetime.date.today()
curr_year = int(curr_date.year)
message = f"Hi {name}, you will be 100 hundred years old in {curr_year + 100 - age} "
print(message)
print()

# Extra 1.1:
repetition = get_integer_input("to define how many times you want me to repeat the message")
print(message * repetition)

# Extra 1.2:
message1 = f"\nHi {name}, you will be 100 hundred years old in {curr_year + 100 - age}"
repetition1 = get_integer_input("to define AGAIN how many times you want me to repeat the message")
print(message1 * repetition1)


# Exercise 2 Checking items if even

number = get_integer_input("to check if it's even")
if number % 2 == 0:
    print("It is even :)")
else:
    print("It is odd :(")
checkpoint("let's run next extra")

# Extra 2.1
number = get_integer_input("to check if it's 4-fold")
if number % 4 == 0:
    print("It is 4-fold :)")
if number % 2 == 0:
    print("It is even :)")
else:
    print("It is odd :(")

# Extra 2.2
checkpoint("to check if the 2nd num is a factor of the 1st")
num_dividend = get_integer_input("to check")
check_divisor = get_integer_input("divide by")
if num_dividend % check_divisor == 0:
    print("Your second number IS a factor to the 1st one :))")
else:
    print("Your second number IS NOT a factor to the 1st one :((")

print("Exercise 3 (and Solution) List items' value size check")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
for i in a:
    if i < 5:
        print(i)
# Extra 3.1a:
b = []
for i in a:
    if i < 5:
        b.append(i)
print(b)
# Extra 3.1b oneliner
print([x for x in a if x < 5])

# Extra 3.2
user_number = get_integer_input("to check if the list contains numbers smaller than yours")
c = []
for i in a:
    if i < user_number:
        c.append(i)
print(c)

# oneliner
print([i for i in a if i < user_number])

# Exercise 4 (and Solution) Number's factor
num4 = get_integer_input("to find all its factors")
for i in range(1, num4 + 1):
    if num4 % i == 0:
        print(i)
checkpoint("to do the same as a list")
print([i for i in range(1, num4 + 1) if num4 % i == 0])


# Exercise 5 (and Solution) List's intersection
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def intersection(aa, bb):
    aabb = list(set([ii for ii in aa if ii in bb]))
    return aabb


print(intersection(a, b))

# Extra. Randomly generate two lists to test this
seq_size = get_integer_input("to define the number range")
list_size = get_integer_input("to define the list size")
while list_size > seq_size:
    list_size = get_integer_input("A SMALLER NUMBER (!!!) to define the list size")
c = random.sample(range(seq_size), list_size)
print("c is:", c)
d = random.sample(range(seq_size), list_size)
print("d is:", d)
print(intersection(c, d))
