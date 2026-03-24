import tkinter as tk


class HangmanCanvas(tk.Canvas):
    GALLOWS_COLOR = "#A0AEC0"
    BODY_COLOR = "#FC6464"

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            width=260,
            height=240,
            bg="#1A202C",
            highlightthickness=0,
            **kwargs,
        )

    # ── Public

    def draw(self, wrong_count: int):
        self.delete("all")
        self._draw_gallows()
        self._draw_body(wrong_count)

    def set_bg(self, color: str):
        self.configure(bg=color)

    # ── Private

    def _draw_gallows(self):
        c = self.GALLOWS_COLOR
        self.create_line(50, 230, 200, 230, fill=c, width=3)  # base
        self.create_line(100, 230, 100, 30, fill=c, width=3)  # pole
        self.create_line(100, 30, 200, 30, fill=c, width=3)  # beam
        self.create_line(200, 30, 200, 60, fill=c, width=3)  # rope

    def _draw_body(self, n: int):
        c = self.BODY_COLOR

        if n >= 1:  # Head
            self.create_oval(180, 60, 220, 100, outline=c, width=3)

        if n >= 2:  # Body
            self.create_line(200, 100, 200, 160, fill=c, width=3)

        if n >= 3:  # Left arm
            self.create_line(200, 115, 170, 145, fill=c, width=3)

        if n >= 4:  # Right arm
            self.create_line(200, 115, 230, 145, fill=c, width=3)

        if n >= 5:  # Left leg
            self.create_line(200, 160, 170, 200, fill=c, width=3)

        if n >= 6:  # Right leg + X eyes
            self.create_line(200, 160, 230, 200, fill=c, width=3)
            # X eyes
            self.create_line(188, 70, 196, 78, fill=c, width=2)
            self.create_line(196, 70, 188, 78, fill=c, width=2)
            self.create_line(204, 70, 212, 78, fill=c, width=2)
            self.create_line(212, 70, 204, 78, fill=c, width=2)
