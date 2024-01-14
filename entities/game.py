from entities.attempt import Attempt
from random import choice

from enums.letter_type import LetterType


class Game:
    answer: str
    attempts: list[Attempt]
    is_win: bool

    def __init__(self):
        from env import Env
        self.answer = choice(Env.words)
        self.attempts = []
        self.is_win = False

    def add_attempts(self, word: str):
        count_letters = len(self.answer)
        self.attempts.append(Attempt(word, self.answer, count_letters))
        count = 0
        for l in self.attempts[-1].letters:
            if l.type == LetterType.RIGHT:
                count += 1
        if count == count_letters:
            self.is_win = True
