"""Create a program with the following:"""
from my_functions import checkpoint, get_integer_input

checkpoint("to do Task A")
a = 7
b = 44.3
print(f"a = {a}, b = {b}.")
print("3. Print the result of adding 'a' to 'b':", a + b)
print("4. Print the result of multiplying 'a' by 'b':", a * b)
print(f"Should be:, {round((a * b), 1)}. IMHO, this is a very stupid bug with floats, will they ever fix it?")
print("5. Print the result of dividing 'b' by 'a':", b / a, "\n")

checkpoint("to do Task B")
print("B. What will be the values of a, b, c at the end?")
print("a = 9, c = 15, b = 8", "\n")

checkpoint("to do Task C")
print("C.Is there a difference between the two lines below? Why?")
print("We should not use left or right quotation marks as they will produce errors")
name1 = "john"
name2 = 'john'
print("There won't be difference between singular and double marks usage.")
print(f"Compare! This is \"john\": {name1}, and this is 'john': {name2}.")

checkpoint("to explain what is the issue with the code below")
my_number = 5 + 5
print("'result is: \"+my_number)\"'")
print("The issue is: we have a plus of a coma. When corrected the result is: ", my_number, "\n")

checkpoint("to do Task D")
print("What will be the output?")
x: int = 5
y: float = 2.36
print(f"x = {x}, y = {y}")
print("The result will be float: ", x + y)
print("The result will be int if we make y the int: ", x + int(y), "\n")

checkpoint("to do Task E")
print("Give me numbers and I will compare the 1st one against the 2nd one.", "\n",
      "Important: Adding equals will end the task")
e = 1
ee = 2
while e != ee:
    e = get_integer_input("input x")
    ee = get_integer_input("input y")
    if e > ee:
        print("BIG")
    elif e < ee:
        print("small")
    else:
        print("They are equal.")
print("End of the task.\n")

checkpoint("to do Task F")
print("Print the season")
k: int = 1
try:
    while 1 <= k <= 4:
        k = get_integer_input("Give me a number between 1 and 4\n Important: other numbers will end the task")
        if k == 1:
            print(k, "is for summer")
        elif k == 2:
            print(k, "is for winter")
        elif k == 3:
            print(k, "is for fall")
        elif k == 4:
            print(k, "is for spring")
        else:
            print("Thanks. End of the task \n")
except ValueError:
    print("Thanks. End of the task \n")

print()
checkpoint("to do the CHALLENGE")
print("Fix the following code without changing a or b:")
a = 8
b = "123"
# print(a+b)
print("a =", a, " and b = \"", b, "\"", sep="")
print("to get an integer sum: a+int(b) = ", a + int(b))
print("to get an string concatenation: str(a)+b = \"", str(a) + b, "\"", sep="")
