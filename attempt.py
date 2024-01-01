from letter import Letter


class Attempt:
    letters: list[Letter]

    def __init__(self, word: str, answer: str):
        self.letters = []
        for i in range(5):
            letter = word[i]
            if letter in answer:
                if letter == answer[i]:
                    letter_type = 1
                else:
                    letter_type = 2
            else:
                letter_type = 0
            self.letters.append(Letter(letter, letter_type))
