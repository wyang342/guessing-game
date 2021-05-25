import random


class GuessingGame():
    answer = 0
    is_solved = False

    def __init__(self, answer):
        self.answer = answer

    def solved(self):
        return self.is_solved

    def guess(self, user_guess):
        if (type(user_guess) == str):
            user_guess = int(user_guess)
        if (user_guess == self.answer):
            self.is_solved = True
            return 'correct'
        if (user_guess > self.answer):
            return 'high'
        else:
            return 'low'


# game = GuessingGame(10)

# print(game.solved())   # => False

# print(game.guess(5))  # => 'low'
# print(game.guess(20))  # => 'high'
# print(game.solved())   # => False

# print(game.guess(10))  # => 'correct'
# print(game.solved())   # => True


# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1, 100))
last_guess = None
last_result = None

while game.solved() == False:
    if last_guess != None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")

    last_guess = input("Enter your guess: ")
    last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")
