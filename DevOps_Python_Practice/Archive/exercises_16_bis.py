import requests
import random
from lxml import html
from typing import Any
from my_functions import get_integer_input
from my_functions.constants import list_digits, list_letters_lowercase, list_letters_uppercase, list_specials


class PasswordParams:
    @staticmethod
    def get_password_type() -> str:
        print("Please select the type of the password.")
        password_type_int: str = ""
        while password_type_int not in ('words', 'chars'):
            password_type_int = input("Print either 'words' or 'chars'")
        print("Thanks! Your type is: ", password_type_int, "\n")
        return password_type_int

    @staticmethod
    def get_password_length() -> int:
        print("Please select the length of the password.")
        password_length_int: int = get_integer_input("to define your password's length")
        print("Thanks! Your type is: ", password_length_int, "\n")
        return password_length_int

    @staticmethod
    def get_password_strength() -> int:
        print("Please select the strength of the password.")
        password_strength_int: str = ""
        while password_strength_int not in ('1', '2', '3', '4'):
            password_strength_int = input("Print either '1', '2', '3', or '4'")
        print("Thanks! Your strength is: ", password_strength_int, "\n")
        return int(password_strength_int)


class PasswordResources:
    @staticmethod
    def generate_word_list(password_strength: int) -> list[str]:
        password_strength *= 3
        word_link: str = f"https://wordfinder.yourdictionary.com/letter-words/{password_strength}/"
        page: Any = requests.get(word_link)
        tree: Any = html.fromstring(page.content)
        word_list_int: list[str] = list(tree.xpath('//td[@class="table__cell table__cell--first"]/text()'))
        return word_list_int

    @staticmethod
    def generate_char_list(password_strength: int) -> list[int | str]:
        if password_strength == 1:
            char_list_int: list[int | str] = list_digits
        elif password_strength == 2:
            char_list_int = list_digits + list_letters_lowercase
        elif password_strength == 3:
            char_list_int = list_digits + list_letters_lowercase + list_letters_uppercase
        else:
            char_list_int = (list_digits + list_letters_lowercase +
                             list_letters_uppercase + list_specials)
        return char_list_int


def generate_password_of_words(word_list_ext: list[str], password_length_ext: int):
    password_length_int = password_length_ext
    password_word_list_int: list[str] = random.sample(word_list_ext, k=password_length_int)
    password_of_words_int: str = ""
    for i in password_word_list_int:
        password_of_words_int += str(i) + " "
    return password_of_words_int


def generate_password_of_chars(char_list_ext: list[int | str], password_length_ext: int):
    password_length_int = password_length_ext * 4
    password_chars_list = random.choices(char_list_ext, k=password_length_int)
    password_of_chars_int: str = ""
    for i in password_chars_list:
        password_of_chars_int += str(i) + ""
    return password_of_chars_int


def generate_password(action="y"):
    print("Hello. Let's start with a new password for you!")
    password_type = PasswordParams.get_password_type()
    password_strength = PasswordParams.get_password_strength()
    password_length = PasswordParams.get_password_length()
    word_list = PasswordResources.generate_word_list(password_strength)
    char_list = PasswordResources.generate_char_list(password_strength)
    password = ""
    while action == "y":
        if password_type == "words":
            password = generate_password_of_words(word_list, password_length)
            print(f"Your password is:  '{password}'")
        else:
            password = generate_password_of_chars(char_list, password_length)
            print(f"Your password is:  '{password}'")
        action = input("If you want to do it again, enter 'y'. We' 'll take anything else as 'no'")
    else:
        print("Thanks for playing with us!")
    return password


password1 = generate_password()
