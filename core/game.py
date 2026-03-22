import random
from data.words import WORD_BANK

MAX_WRONG = 5


class HangmanGame:
    def __init__(self):
        self.secret_word = ""
        self.hint = ""
        self.category = ""
        self.guessed: set[str] = set()
        self.wrong_count = 0

    # ── New round

    def new_game(self):
        self.category = random.choice(list(WORD_BANK.keys()))
        word, hint = random.choice(WORD_BANK[self.category])
        self.secret_word = word.upper()
        self.hint = hint
        self.guessed = set()
        self.wrong_count = 0

    # ── Guess

    def guess(self, letter: str) -> bool:
        letter = letter.upper()

        if letter in self.guessed:
            raise ValueError(f"'{letter}' already guessed.")

        self.guessed.add(letter)

        if letter in self.secret_word:
            return True
        else:
            self.wrong_count += 1
            return False

    # ── State checks

    def is_won(self) -> bool:
        return all(l in self.guessed for l in self.secret_word)

    def is_lost(self) -> bool:
        return self.wrong_count >= MAX_WRONG

    def is_over(self) -> bool:
        return self.is_won() or self.is_lost()

    def attempts_left(self) -> int:
        return MAX_WRONG - self.wrong_count

    def word_display(self) -> str:
        return "  ".join(l if l in self.guessed else "_" for l in self.secret_word)

    def wrong_letters(self) -> list[str]:
        return [l for l in self.guessed if l not in self.secret_word]
