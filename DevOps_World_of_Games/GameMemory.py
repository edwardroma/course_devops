from my_functions import checkpoint, get_integer_input
import secrets


class GameMemory:
    def __init__(self, game_dif_ext):
        self.result = ""
        self.sequence_app = ()
        self.sequence_user = ""
        self.game_num = ""
        self.game_dif_ext = game_dif_ext
        self.game_dif_int = ""

    def set_difficulty_int(self):
        self.game_dif_int = get_integer_input("to define the difficulty level")

    def generate_sequence(self):
        self.sequence_app = []
        while len(self.sequence_app) <= int(self.game_dif_int):
            self.sequence_app.append(secrets.choice(range(1, 101)))
        print("Here is your sequence for testing purposes:", self.sequence_app)
        return self.sequence_app

    def get_list_from_user(self):
        self.sequence_user = []
        while len(self.sequence_user) <= int(self.game_dif_int):
            y = get_integer_input("to form your own list")
            self.sequence_user.append(y)
        print("Your list is: ", self.sequence_user)
        return self.sequence_user

    def is_list_equal(self):
        checkpoint("to compare the lists")
        self.sequence_app = sorted(self.sequence_app)
        self.sequence_user = sorted(self.sequence_user)
        if self.sequence_app == self.sequence_user:
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
            self.generate_sequence()
            self.get_list_from_user()
            self.is_list_equal()
            print(self.result)
            print("Wanna try again? (NB: We'll take 'go' -  for 'Yes', and anything else for 'No)")
            action = input("So, what would you say? :")
        else:
            print("Thanks for playing with us. See you next game!)")


if __name__ == "__main__":
    game1 = GameMemory(4)
    game1.play()
