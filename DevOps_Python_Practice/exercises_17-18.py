# import requests
# from bs4 import BeautifulSoup
# import lxml
# from typing import reveal_type, Any
import random
from my_functions import get_integer_input

"""Exercise 17 (and Solution) Decode A Web Page"""
# # print out a list of all the article titles on the New York Times homepage.
# url = 'https://www.nytimes.com/'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")
# news: list[Any] = soup.findAll(class_="indicate-hover css-66vf3i")
# [print(x.get_text()) for x in news]

'''Exercise 18 (and Solution) Cows And Bulls'''
# Randomly generate a 4-digit number.


def get_number_from_app():
    number_length_int = get_integer_input("to define the length of randomly generate number")
    digits_picked_int = [str(x) for x in random.sample(range(0, 10), k=number_length_int)]
    print(digits_picked_int)
    number_picked_int = ""
    for d in digits_picked_int:
        number_picked_int += str(d)
    return number_length_int, digits_picked_int


def get_number_from_user():
    number_guessed_int = input("guess the picked number")
    digits_guessed_int = list(number_guessed_int)
    return digits_guessed_int


def compare_lists(number_length_int, digits_picked_int, digits_guessed_int):
    count_bulls_int = 0
    for y in range(number_length_int):
        if digits_guessed_int[y] == digits_picked_int[y]:
            count_bulls_int += 1
        else:
            pass
    print(f"count BULLS is:{count_bulls_int}")
    count_cows_int = -count_bulls_int
    for x in range(number_length_int):
        if digits_guessed_int[x] in digits_picked_int:
            count_cows_int += 1
    print("cows: ", count_cows_int)
    return count_bulls_int


def play():
    count_bulls = ""
    number_length, digits_picked = get_number_from_app()
    while count_bulls != number_length:
        digits_guessed = get_number_from_user()
        count_bulls = compare_lists(number_length, digits_picked, digits_guessed)
        print("Wrong (... Try again")
    else:
        print("You won!")
        print("Thanks for playing with us!")


if __name__ == "__main__":
    play()
