import random
import requests
from lxml import html
from my_functions import get_integer_input

list_numbers = [x for x in range(0, 10)]
list_letters_lowercase = [chr(x) for x in range(ord('a'), ord('z') + 1)]
list_letters_uppercase = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
string_specials = list('@_!#$%^&*()<>?/\\|}{~:,.')
list_specials = [x for x in string_specials]


class PasswDetails:
    @staticmethod
    def get_passw_type() -> str:
        print("\nPlease type what specifically your password should consist of.")
        passw_type = input("Please type in 'words' or 'characters'.")
        while passw_type not in ("words", "characters"):
            print("Sorry, either 'words' or 'characters', no other options admitted.")
            passw_type = input("\nWhich password would you like to create? 'words' or 'characters'?")
        else:
            print(f"Thanks!Your Type is a '{passw_type}' password.\n")
        return passw_type

    @staticmethod
    def get_passw_length() -> int:
        """Let user define the length of future password"""
        passw_length = get_integer_input("to define the password length")
        print(f"Thanks! The length of your password is '{passw_length}' words or specs in the password.\n")
        return passw_length

    @staticmethod
    def get_passw_strength() -> int:
        print("Now we need to define the password's complexity.")
        print("It can be: '1' for 'easy, '2' for 'simple', 3 for 'middle', or 4 for 'complex'?")
        passw_strength = get_integer_input("to specify your password strength")
        while passw_strength not in (1, 2, 3, 4):
            print("Sorry, either '1', '2', '3' or '4', no other options admitted.")
            print("\nWhich password would you like to create?")
            passw_strength = int(input("'1' for 'easy, '2' for 'simple', 3 for 'middle', or 4 for 'complex'?"))
        else:
            print(f"Your Complexity is {passw_strength}.")
        return passw_strength


class PasswResources:
    def __init__(self, passw_length, passw_strength):
        self.passw_length = passw_length
        self.word_link = ""
        self.word_list = ""
        self.passw_strength = passw_strength

    def gen_word_link(self, passw_strength):
        if passw_strength == 1:
            passw_strength = "2"
        elif passw_strength == 2:
            passw_strength = "6"
        elif passw_strength == 3:
            passw_strength = "10"
        elif passw_strength == 4:
            self.passw_strength = "15"
        self.word_link = f"https://wordfinder.yourdictionary.com/letter-words/{passw_strength}/"
        return self.word_link

    def gen_word_list(self, word_link_ext):
        """Generates the list of words basing on those present on the corresponding link/page"""
        page = requests.get(word_link_ext)
        tree = html.fromstring(page.content)
        self.word_list = list(tree.xpath('//td[@class="table__cell table__cell--first"]/text()'))
        return self.word_list

    @staticmethod
    def gen_char_list(passw_strength):
        if passw_strength == 1:
            char_list = list_numbers
        elif passw_strength == 2:
            char_list = list_numbers + list_letters_lowercase
        elif passw_strength == 3:
            char_list = list_numbers + list_letters_lowercase + list_letters_uppercase
        else:
            char_list = list_numbers + list_letters_lowercase + list_letters_uppercase + list_specials
        return char_list


def gen_passw_of_words(word_list, passw_length_ext):
    passw_length_int = passw_length_ext
    passw_word_list = random.sample(word_list, k=passw_length_int)
    passw_of_words = ""
    for i in passw_word_list:
        passw_of_words += str(i) + " "
    return passw_of_words


def gen_passw_of_chars(char_list_ext, passw_length_ext):
    passw_length_int = passw_length_ext * 4
    passw_chars_list = random.sample(char_list_ext, k=passw_length_int)
    passw_of_chars = ""
    for i in passw_chars_list:
        passw_of_chars += str(i) + ""
    return passw_of_chars


def gen_passw(passw_type_ext, passw_of_words, passw_of_chars):
    passw = ""
    if passw_type_ext == "words":
        passw = passw_of_words
    elif passw_type_ext == "characters":
        passw = passw_of_chars
    print("Your INT password is: ", passw)
    return passw


def password_generation():
    # Instantiate Details
    passw_detail_1 = PasswDetails()
    # Get from user: Type, Length, Strength
    passw_type = passw_detail_1.get_passw_type()
    passw_length = passw_detail_1.get_passw_length()
    passw_strength = passw_detail_1.get_passw_strength()
    # Generate by user input: word_link >> word_list
    passw_resource_1 = PasswResources(passw_length, passw_strength)
    word_link = passw_resource_1.gen_word_link(passw_strength)
    word_list = passw_resource_1.gen_word_list(word_link)
    # Generate by user input: passw_strength >> char_list
    char_list = passw_resource_1.gen_char_list(passw_strength)
    # Generate passwords - of words or pof chars
    passw_of_words = gen_passw_of_words(word_list, passw_length)
    passw_of_chars = gen_passw_of_chars(char_list, passw_length)
    passw = gen_passw(passw_type, passw_of_words, passw_of_chars)
    return passw


def main_function(action="yes"):
    """The 'wrapping' function allowing the user to call the password generator several times."""
    print("Hello. Let's start with a new password for you!")
    password = ""
    while action == "yes":
        password = password_generation()
        action = input("If you want to do it again, enter 'yes'. We'' take anything else as 'no'")
    else:
        print("Thanks for playing with us!")
    print("Your password is:", password)


main_function()
