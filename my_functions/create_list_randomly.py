import random


def create_list_randomly():
    seq_size = int(input("How long is the range to form a list?"))
    list_size = int(input("How long the list do you need?"))
    lst = random.sample(range(seq_size+1), k=list_size)
    return sorted(lst)


if __name__ == "__main__":
    print(create_list_randomly)
