import random
from my_functions import get_integer_input
# Exercise 11 (and Solution) Check Primality Functions


def is_int_prime():
    user_number = get_integer_input("to check it is prime")
    count = 0
    for x in range(1, user_number+1):
        if user_number % x == 0:
            count += 1
            print(x)
    if count > 2:
        result = "It is a prime!"
    else:
        result = "It is NOT a prime ("
    return result


print(is_int_prime())


# Exercise 12 (and Solution) List Ends
def list_ends():
    list_end = get_integer_input("Give me the list ends")
    list_max = get_integer_input("Give me the list max")
    list_size = get_integer_input("Give me the list size")
    a = random.sample(range(1, list_max), list_size)
    print(a)
    aa = sorted(a)
    print(aa)
    b = [aa[0], aa[-1]]
    print("this is b:", b)
#    print(aa[list_end-1])
    print("one but-start element", aa[list_end-1])
    print("one but-end element", aa[-list_end])
    bb = [aa[0:list_end]]
    bbb = [aa[-list_end:]]
    print("start elements", bb)
    print("end elements", bbb)


# Exercise 13 (and Solution) Fibonacci
def fibo():
    a = count = 0
    b = 1
    c = []
    range1 = get_integer_input("to define the size of the sequence")
    while count < range1:
        c.append(a)
        a, b = b, a+b
        count += 1
    return c


print(fibo())

# Exercise 14 (and Solution) List Remove Duplicates
lst1 = [1, 3, 1, 54, 34, 54, 324, 65, 3, 567, 35, 75, 23, 57]


def rem_dup1(lst):
    new_lst = list(set(lst))
    return new_lst


print("main ex: ", rem_dup1(lst1))


# Extra: using a loop and constructing a list
def remove_duplicates2(lst):
    lst2 = [x for x in lst if x not in lst]
    print(lst2)
    lst2 = []
    for x in lst:
        if x not in lst2:
            lst2 = lst2 + [x]
    print("extra: ", lst2)


remove_duplicates2(lst1)


# Printing Lists
def print_lists():
    print("list in one row: ", [x for x in range(5)])
    [print("list item per row []", x) for x in range(5)]
    {print("list item per row {}", x) for x in range(5)}
    print("tuple:", tuple(range(5)))


print_lists()


# Exercise 15 (and Solution) Reverse Word Order
def reverse_order():
    string1 = input("Give me a string:")
    split1 = string1.split()
    split1.reverse()
    string2 = " ".join(split1)
    print(string2)
    pass


reverse_order()
