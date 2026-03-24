import customtkinter as ctk
from core.game import HangmanGame
from gui.sidebar import Sidebar
from gui.canvas import HangmanCanvas


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title("🎮 Hangman Game")
        self.geometry("860x640")
        self.resizable(False, False)
        self._game = HangmanGame()
        self._wins = 0
        self._losses = 0
        self._dark = True
        self._key_btns: dict[str, ctk.CTkButton] = {}
        self._build_ui()
        self._new_game()

    # ── UI Construction

    def _build_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._sidebar = Sidebar(
            self,
            on_new_game=self._new_game,
            on_toggle_theme=self._toggle_theme,
        )
        self._sidebar.grid(row=0, column=0, sticky="nsew")
        right = ctk.CTkFrame(self, corner_radius=0, fg_color="#171923")
        right.grid(row=0, column=1, sticky="nsew")
        right.grid_columnconfigure(0, weight=1)
        canvas_card = ctk.CTkFrame(right, corner_radius=12, fg_color="#1A202C")
        canvas_card.grid(row=0, column=0, padx=24, pady=(20, 8), sticky="ew")
        self._canvas = HangmanCanvas(canvas_card)
        self._canvas.pack(pady=10)
        self._word_lbl = ctk.CTkLabel(
            right,
            text="",
            font=ctk.CTkFont(family="Consolas", size=30, weight="bold"),
        )
        self._word_lbl.grid(row=1, column=0, pady=(8, 2))

        ctk.CTkLabel(
            right,
            text="Wrong letters:",
            font=ctk.CTkFont(size=11),
            text_color="#718096",
        ).grid(row=2, column=0)

        self._wrong_lbl = ctk.CTkLabel(
            right,
            text="—",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#FC6464",
        )
        self._wrong_lbl.grid(row=3, column=0, pady=(0, 4))

        self._status_lbl = ctk.CTkLabel(
            right,
            text="",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self._status_lbl.grid(row=4, column=0, pady=(0, 6))
        kb_card = ctk.CTkFrame(right, corner_radius=12, fg_color="#1A202C")
        kb_card.grid(row=5, column=0, padx=24, pady=(0, 20), sticky="ew")
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        for r, letters in enumerate(rows):
            row_frame = ctk.CTkFrame(kb_card, fg_color="transparent")
            row_frame.grid(row=r, column=0, pady=4, padx=10)
            for letter in letters:
                btn = ctk.CTkButton(
                    row_frame,
                    text=letter,
                    width=46,
                    height=40,
                    corner_radius=8,
                    font=ctk.CTkFont(size=13, weight="bold"),
                    fg_color="#2D3748",
                    hover_color="#4A5568",
                    command=lambda l=letter: self._on_guess(l),
                )
                btn.pack(side="left", padx=3, pady=4)
                self._key_btns[letter] = btn

    # ── Game flow

    def _new_game(self):
        self._game.new_game()
        self._sidebar.update_category(self._game.category)
        self._sidebar.update_attempts(self._game.attempts_left())
        self._sidebar.set_hint(self._game.hint)
        self._sidebar.reset_hint()
        self._status_lbl.configure(text="")
        self._wrong_lbl.configure(text="—")
        self._word_lbl.configure(text_color="#FFFFFF")
        for btn in self._key_btns.values():
            btn.configure(state="normal", fg_color="#2D3748", text_color="#FFFFFF")

        self._canvas.draw(0)
        self._refresh_word()

    def _on_guess(self, letter: str):
        if self._game.is_over():
            return

        correct = self._game.guess(letter)
        btn = self._key_btns[letter]

        if correct:
            btn.configure(fg_color="#276749", state="disabled")
        else:
            btn.configure(fg_color="#822727", state="disabled")
            self._sidebar.update_attempts(self._game.attempts_left())

        self._canvas.draw(self._game.wrong_count)
        self._refresh_word()
        self._refresh_wrong()
        self._check_end()

    def _check_end(self):
        if self._game.is_won():
            self._wins += 1
            self._sidebar.update_score(self._wins, self._losses)
            self._status_lbl.configure(
                text=f"🎉 You Won!  Word: {self._game.secret_word}",
                text_color="#48C78E",
            )
            self._disable_keyboard()

        elif self._game.is_lost():
            self._losses += 1
            self._sidebar.update_score(self._wins, self._losses)
            self._status_lbl.configure(
                text=f"💀 Game Over!  Word: {self._game.secret_word}",
                text_color="#FC6464",
            )
            self._disable_keyboard()

    # ── Helpers

    def _refresh_word(self):
        self._word_lbl.configure(text=self._game.word_display())

    def _refresh_wrong(self):
        wrong = self._game.wrong_letters()
        self._wrong_lbl.configure(text="  ".join(wrong) if wrong else "—")

    def _disable_keyboard(self):
        for btn in self._key_btns.values():
            btn.configure(state="disabled")

    def _toggle_theme(self):
        self._dark = not self._dark
        if self._dark:
            ctk.set_appearance_mode("dark")
            self._canvas.set_bg("#1A202C")
        else:
            ctk.set_appearance_mode("light")
            self._canvas.set_bg("#E2E8F0")
        self._sidebar.update_theme_btn(self._dark)
