class GuessingGame():
    answer = 0
    is_solved = False

    def __init__(self, answer):
        self.answer = answer

    def solved(self):
        return self.is_solved

    def guess(self, user_guess):
        if (user_guess == self.answer):
            self.is_solved = True
            return 'correct'
        if (user_guess > self.answer):
            return 'high'
        else:
            return 'low'


game = GuessingGame(10)

print(game.solved())   # => False

print(game.guess(5))  # => 'low'
print(game.guess(20))  # => 'high'
print(game.solved())   # => False

print(game.guess(10))  # => 'correct'
print(game.solved())   # => True
