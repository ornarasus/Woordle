import settings
from attempt import Attempt
from random import choice


class Game:
    answer: str
    attempts: list[Attempt]
    is_win: bool

    def __init__(self):
        self.answer = choice(settings.words)
        self.attempts = []
        self.is_win = False

    def add_attempts(self, word: str):
        self.attempts.append(Attempt(word, self.answer))
        count = 0
        for l in self.attempts[-1].letters:
            if l.type == 1:
                count += 1
        if count == 5:
            self.is_win = True
