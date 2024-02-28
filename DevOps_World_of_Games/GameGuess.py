from my_functions import checkpoint, get_integer_input
import secrets


class GameGuess:
    def __init__(self, game_dif_ext):
        self.guess_from_user = ""
        self.secret_number = ""
        self.result = ""
        self.game_num = ""
        self.game_dif_ext = game_dif_ext
        self.game_dif_int = ""

    def set_difficulty_int(self):
        print("start")
        self.game_dif_int = get_integer_input("to define the difficulty level")

    def generate_number(self):
        checkpoint("to generate your secret number")
        self.secret_number = secrets.choice(range(1, int(self.game_dif_int)+1))
        print("shh! just between you and me: your secret number is: ", self.secret_number)
        return self.secret_number

    def get_guess_from_user(self):
        self.guess_from_user = get_integer_input("to try and guess the secret number")
        return self.guess_from_user

    def compare_results(self):
        checkpoint("to compare the numbers")
        self.result = ""
        if self.secret_number == self.guess_from_user:
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
            self.generate_number()
            self.get_guess_from_user()
            self.compare_results()
            print(self.result)
            print("Wanna try again? (NB: We'll take 'go' -  for 'Yes', and anything else - for 'No)")
            action = input("So, what would you say? :")
        else:
            print("Thanks for playing with us. See you next game!) ")


if __name__ == "__main__":
    game_guess = GameGuess(4)
    game_guess.play()
