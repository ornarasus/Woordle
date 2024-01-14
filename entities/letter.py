from enums.letter_type import LetterType


class Letter:
    text: str
    type: LetterType

    def __init__(self, letter: str, letter_type: LetterType):
        self.text = letter
        self.type = letter_type
