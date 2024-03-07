import random
from my_functions import checkpoint, get_integer_input

# Exercise 6 (and Solution)

word1 = input("Give me a word to check if this is a palindrome: ")
word2 = word1[::-1]
print(word1, "is a palindrome!!!") if word1 == word2 else print(f"Not a palindrome: {word1} vs {word2}")


# Exercise 7 (and Solution) List manipulations
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# takes this list a and makes a new list that has only the even elements of this list in it.
print([x for x in a if x % 2 == 0])

years_of_birth = [1967, 1987, 1997, 2000, 1940, 1963]
ages = [2024 - year for year in years_of_birth]
print(ages)


# Exercise 8 (and Solution) Rock-Scissors-Paper game
action = "go"
range1 = ("R", "S", "P")
player1 = player2 = ""
while action == "go":
    print("Players! Give me 'R' for 'Rock', 'S' for 'Scissors', or 'P' for 'Paper'.")
    while player1 not in range1:
        player1 = input("Player 1: ").upper()
        break
    else:
        print("")
    while player2 not in range1:
        player2 = input("Player 2: ").upper()
        break
    else:
        print("give me P, R, or S")
    total = player1 + player2
    if total in ("RS", "SP", "PR"):
        print("Player 1 won!")
    elif total in ("RS", "SP", "PR"):
        print("Player 2 won!")
    else:
        print("Ties!!!")
    player1 = player2 = ""
    action = input("do you want to play more? type 'go' if you do. We will take everything else as 'No'...")
else:
    print("Thanks for playing with us. Bye!")

# Exercise 9 (and Solution) Guessing Game One
action = ""
while action != "exit":
    checkpoint("to generate a random number")
    number_random = random.choice(range(1, 9))
    print(number_random)
    number_guess = count_of_guesses = int()
    while number_guess != number_random:
        number_guess = get_integer_input("to guess the random number")
        count_of_guesses += 1
        if number_guess > number_random:
            print("Our number is smaller...")
            pass
        elif number_guess < number_random:
            print("Our number is bigger...")
            pass
    # Extra 1: Keep the game going until the user types “exit”
    else:
        # Extra 2: Keep track of how many guesses the user has taken, and when the game ends, print this out.
        print(f"You are right! It took you {count_of_guesses} attempts to get the correct number!")
        action = input("To exit the game type 'exit', we will take anything else as your wish to play again.")
else:
    print("Thanks for playing with us. Bye!")

# Exercise 10 (and Solution) List Overlap Comprehensions
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(a, b)
c = list(set([x for x in a if x in b]))
print(c)
# Extra: Randomly generate two lists to test this
list_size1 = get_integer_input("to set the 1st list size")
a = random.sample(range(1, 101), list_size1)
list_size2 = get_integer_input("to set the 2nd list size")
b = random.sample(range(1, 101), list_size2)
c = list(set([x for x in a if x in b]))
print(c)
