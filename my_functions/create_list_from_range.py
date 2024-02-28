# Create a list automatically
from my_functions import get_integer_input


def create_list_from_range():
    list_range = []
    list_limit = get_integer_input("to define the list length")
    for i in range(1, list_limit + 1):
        list_range.append(i)
    return list_range


if __name__ == "__main__":
    print(create_list_from_range())
