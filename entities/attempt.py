from entities.letter import Letter
from enums.letter_type import LetterType


class Attempt:
    letters: list[Letter]

    def __init__(self, word: str, answer: str, count_letters: int):
        self.letters = []
        for i in range(count_letters):
            letter = word[i]
            if letter in answer:
                if letter == answer[i]:
                    letter_type = LetterType.RIGHT
                else:
                    letter_type = LetterType.OTHER_PLACE
            else:
                letter_type = LetterType.WRONG
            self.letters.append(Letter(letter, letter_type))
