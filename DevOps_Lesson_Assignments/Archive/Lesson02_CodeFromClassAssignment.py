from my_functions import checkpoint, create_list_manually, create_list_from_range

# Task 1a. Function receives a list of strings.
checkpoint("to define the list length")
x = create_list_from_range()
print(x)

checkpoint("to define the number of items in the list")
y = create_list_manually()
print(y)


# Task 1b. It returns the amount of variables in that list.
def list_items_count(lst):
    count = 0
    for i in lst:
        count += 1
        lst.pop(i)
    return count


x_count = list_items_count(x)
print("The number of items in list generated automatically is:", x_count)

y_count = list_items_count(y)
print("The number of items in list generated manually is:", y_count)


# Task 2
def list_check(pr):
    print("We are working with the dictionary:", pr)
    for key in pr:
        if key == "":
            print(f"\033[1mWe are missing the key for the '{pr[key]}' value \033[0m")
        else:
            print(f"Seems the '{key}' key for the '{pr[key]}' value is in place.")
            if pr[key] == "":
                print(f"\033[1mWe are missing the value of the '{key}' key.\033[0m")
            else:
                print(f"Seems the '{key}' key has its value alright: '{pr[key]}'.")


pr1 = {"Name": "John", "Age": 18, "Hobbies": ["Piano", "Football", "Whiskey"]}
pr2 = {"Name": "John", "": 18, "Hobbies": ["Piano", "Football", "Whiskey"]}
pr3 = {"Name": "John", "Age": '', "": ["Piano", "Football", "Whiskey"]}

list_check(pr1)
print()
list_check(pr2)
print()
list_check(pr3)
