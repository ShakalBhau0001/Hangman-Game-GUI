import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_new_game, on_toggle_theme, **kwargs):
        super().__init__(
            master,
            width=220,
            corner_radius=0,
            fg_color="#1A1A2E",
            **kwargs,
        )
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self._on_new_game = on_new_game
        self._on_toggle_theme = on_toggle_theme
        self._build()

    # ── Build

    def _build(self):
        ctk.CTkLabel(self, text="🎮", font=ctk.CTkFont(size=40)).grid(
            row=0, column=0, pady=(28, 0)
        )

        ctk.CTkLabel(
            self,
            text="Hangman",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#63B3ED",
        ).grid(row=1, column=0)

        ctk.CTkLabel(
            self,
            text="Game",
            font=ctk.CTkFont(size=12),
            text_color="#4A5568",
        ).grid(row=2, column=0, pady=(0, 16))

        # Separator
        self._sep(row=3)

        # Score card
        score_card = ctk.CTkFrame(self, corner_radius=10, fg_color="#2D3748")
        score_card.grid(row=4, column=0, padx=14, pady=10, sticky="ew")
        score_card.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(
            score_card,
            text="🏆  Score",
            font=ctk.CTkFont(size=12, weight="bold"),
        ).grid(row=0, column=0, columnspan=2, pady=(10, 4))

        ctk.CTkLabel(
            score_card,
            text="Wins",
            font=ctk.CTkFont(size=11),
            text_color="#A0AEC0",
        ).grid(row=1, column=0)

        ctk.CTkLabel(
            score_card,
            text="Losses",
            font=ctk.CTkFont(size=11),
            text_color="#A0AEC0",
        ).grid(row=1, column=1)

        self._wins_lbl = ctk.CTkLabel(
            score_card,
            text="0",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#48C78E",
        )
        self._wins_lbl.grid(row=2, column=0, pady=(0, 10))

        self._losses_lbl = ctk.CTkLabel(
            score_card,
            text="0",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#FC6464",
        )
        self._losses_lbl.grid(row=2, column=1, pady=(0, 10))

        # Category
        ctk.CTkLabel(
            self,
            text="Category",
            font=ctk.CTkFont(size=11),
            text_color="#4A5568",
        ).grid(row=5, column=0, pady=(10, 2))

        self._cat_lbl = ctk.CTkLabel(
            self,
            text="—",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#F6AD55",
        )
        self._cat_lbl.grid(row=6, column=0)

        # Attempts left
        ctk.CTkLabel(
            self,
            text="Attempts Left",
            font=ctk.CTkFont(size=11),
            text_color="#4A5568",
        ).grid(row=7, column=0, pady=(10, 2))

        self._attempts_lbl = ctk.CTkLabel(
            self,
            text="6",
            font=ctk.CTkFont(size=30, weight="bold"),
            text_color="#63B3ED",
        )
        self._attempts_lbl.grid(row=8, column=0)

        # Hint button + label
        self._hint_btn = ctk.CTkButton(
            self,
            text="💡  Show Hint",
            height=34,
            corner_radius=8,
            fg_color="#744210",
            hover_color="#975A16",
            font=ctk.CTkFont(size=12),
            command=self._show_hint,
        )
        self._hint_btn.grid(row=9, column=0, padx=14, pady=(14, 4), sticky="ew")

        self._hint_lbl = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=11, slant="italic"),
            text_color="#F6AD55",
            wraplength=190,
        )
        self._hint_lbl.grid(row=10, column=0, padx=14)

        # Spacer
        self.grid_rowconfigure(11, weight=1)

        # Separator
        self._sep(row=12)

        # Theme toggle
        self._theme_btn = ctk.CTkButton(
            self,
            text="☀  Light Mode",
            height=34,
            corner_radius=8,
            fg_color="#2D3748",
            hover_color="#4A5568",
            font=ctk.CTkFont(size=12),
            text_color="#A0AEC0",
            command=self._on_toggle_theme,
        )
        self._theme_btn.grid(row=13, column=0, padx=12, pady=(8, 4), sticky="ew")

        # New game button
        ctk.CTkButton(
            self,
            text="🔄  New Game",
            height=38,
            corner_radius=8,
            fg_color="#2B4C7E",
            hover_color="#1A365D",
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._on_new_game,
        ).grid(row=14, column=0, padx=12, pady=(4, 20), sticky="ew")

    # ── Public Methods

    def update_score(self, wins: int, losses: int):
        self._wins_lbl.configure(text=str(wins))
        self._losses_lbl.configure(text=str(losses))

    def update_category(self, category: str):
        self._cat_lbl.configure(text=category)

    def update_attempts(self, attempts: int):
        color = "#48C78E" if attempts > 3 else "#F6AD55" if attempts > 1 else "#FC6464"
        self._attempts_lbl.configure(text=str(attempts), text_color=color)

    def set_hint(self, hint: str):
        self._hint = hint
        self._hint_lbl.configure(text="")
        self._hint_btn.configure(state="normal")

    def update_theme_btn(self, dark: bool):
        self._theme_btn.configure(text="☀  Light Mode" if dark else "🌙  Dark Mode")

    def reset_hint(self):
        self._hint_lbl.configure(text="")
        self._hint_btn.configure(state="normal")

    # ── Private

    def _show_hint(self):
        self._hint_lbl.configure(text=f"💡 {self._hint}")
        self._hint_btn.configure(state="disabled")

    def _sep(self, row: int):
        ctk.CTkFrame(self, height=1, fg_color="#2D3748").grid(
            row=row, column=0, sticky="ew", padx=14, pady=4
        )

    # Internal hint store
    _hint: str = ""
