"""Create a list manually"""


def create_list_manually():
    print("NB: 'Empty' input terminates the list.")
    list_manual = []
    list_item = 1
    while list_item != "":
        list_item = input("Please give a str: ")
        list_manual.append(list_item)
    else:
        list_manual.pop()
    return list_manual


if __name__ == "__main__":
    print("test completed: ", create_list_manually())
