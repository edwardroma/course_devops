from GameMemory import GameMemory
from GameGuess import GameGuess
from GameCurrency import GameCurrency


def welcome(name):
    # name = input("Please give me your name: ")
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    print("\nRight now we have for you:\n"
          "        1. Memory Game - a sequence of numbers will appear for 1 second "
          "and you have to guess it back.\n"
          "        2. Guess Game - guess a number and see if you choose like the "
          "computer.\n"
          "        3. Currency Roulette - try and guess the value of a random amount "
          "of USD in ILS.\n")
    game_num, game_dif_ext = get_game_inputs()
    game1 = GameMemory(game_dif_ext)
    game2 = GameGuess(game_dif_ext)
    game3 = GameCurrency(game_dif_ext)
    game1.play() if game_num == 1 else game2.play() if game_num == 2 else game3.play()


def get_game_inputs():
    while True:
        try:
            game_num = int(input('Please enter your game number (1, 2, or 3): '))
            if game_num > 3 or game_num < 1:
                print('Please Choose 1 (Memory Game), 2 (Guess Game), or 3 (Currency Roulette):')
                print(game_num)
            else:
                print(f'You have chosen game # {game_num}')
                break
        except ValueError:
            print(f"Your input does look like an integer. Let's try again...")
    while True:
        try:
            game_dif_ext = int(input('Please enter your game difficulty level (between 1 and 5): '))
            if game_dif_ext > 5 or game_dif_ext < 1:
                print('Please Choose 1-5:')
                continue
            else:
                print(f'You have chosen game difficulty level # {game_dif_ext}')
                break
        except ValueError:
            print(f"Your input does look like an integer. Let's try again...")
    return game_num, game_dif_ext
