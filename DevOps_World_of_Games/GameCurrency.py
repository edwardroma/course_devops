import random
import requests
from my_functions import checkpoint, get_integer_input


class GameCurrency:
    def __init__(self, game_dif_ext):
        self.shekel_rate = ""
        self.limit1 = ""
        self.limit2 = ""
        self.guess = ""
        self.result = ""
        self.guess_from_user = ""
        self.secret_number = ""
        self.game_num = ""
        self.game_dif_ext = game_dif_ext
        self.game_dif_int = ""

    def set_difficulty_int(self):
        self.game_dif_int = get_integer_input("to define the difficulty level - up to 5")

    def get_shekel_rate(self):
        url = "https://v6.exchangerate-api.com/v6/617730a39f8a17d511fe6315/latest/USD"
        rates = requests.get(url)
        self.shekel_rate = rates.json()["conversion_rates"]["ILS"]
        return self.shekel_rate

    def get_guess_from_user(self):
        random_number = int(random.randint(1, 10))
        total = self.shekel_rate * random_number
        self.limit1 = int(total) - (5 + int(self.game_dif_int))
        if self.limit1 < 0:
            self.limit1 = 0
        else:
            pass
        print("For testing purposes, self.limit1 is: ", self.limit1)
        self.limit2 = int(total) + (5 + int(self.game_dif_int))
        print("For testing purposes, self.limit2 is: ", self.limit2)
        print("FYI, the correct answer for testing purposes is: ", total)
        self.guess = get_integer_input(f"gimme your shekel amount for {random_number} dollars")

    def is_get_correct(self):
        checkpoint("to compare the lists")
        if self.guess in range(int(self.limit1), int(self.limit2)):
            self.result = "True! - You won!!!"
        else:
            self.result = "False - You lost ((( ..."
        return self.result

    def play(self):
        action = "go"
        while action == "go":
            if self.game_dif_ext != "":
                self.game_dif_int = self.game_dif_ext
            else:
                self.set_difficulty_int()
            self.game_dif_ext = ""
            self.get_shekel_rate()
            self.get_guess_from_user()
            self.is_get_correct()
            print(self.result)
            print("Wanna try again? (NB: We'll take 'go' -  for 'Yes', and anything else for 'No)")
            action = input("So, what would you say? :")
        else:
            print("Thanks for playing with us. See you next game!) ")


if __name__ == "__main__":
    game_currency = GameCurrency(4)
    game_currency.play()
