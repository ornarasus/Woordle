class Letter:
    text: str
    """ type:
    0 - отсутствует
    1 - на правильном месте
    2 - на неправильном месте
    """
    type: int

    def __init__(self, letter: str, letter_type: int):
        self.text = letter
        self.type = letter_type
