# 🎮 Hangman-Game-GUI 🔤

A modern, feature-rich desktop Hangman game built with **CustomTkinter**.It offers a sleek user interface with sidebar navigation, an on-screen keyboard, animated hangman drawing, multiple word categories, a hint system, and a live score tracker for a complete gaming experience.

---

## 🧱 Project Structure

```bash
Hangman-Game-GUI/
│
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── assets/                  # Images and assets for the GUI
├── core/                    # Game logic modules
│   └── game.py              # Hangman game mechanics
├── data/                    # Game data
│   └── words.py             # Word lists for categories
├── gui/                     # User interface components
│   └── sidebar.py           # Sidebar navigation UI
└── README.md                # Project documentation
```

---

## ✨ Features

### 🎮 Gameplay
- **Classic Hangman rules** – guess letters to uncover a hidden word before the hangman is fully drawn
- **4 distinct word categories – choose from different themes for varied gameplay
- **On-screen A-Z keyboard** – fully interactive with visual feedback
- **Hint system** – get clues when you're stuck
- **Live score tracker** – keep track of your wins and losses

### 🖥 GUI Highlights
- Modern, dark-themed interface using **CustomTkinter**
- **Sidebar navigation** for smooth category switching
- **Animated hangman drawing** – each wrong guess adds a part of the hangman
- Responsive layout with clear visual feedback for correct/wrong guesses
- Category selection menu with icons

---

## 🛠 Technologies Used

| Technology | Role |
| ---------- | ---- |
| **Python 3** | Core programming language |
| **CustomTkinter** | Modern GUI framework |
| **Pillow (PIL)** | Image processing for assets |
| **Random** | Word selection and game variation |
| **Tkinter** | Base UI components |

---

## 📌 Requirements

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install customtkinter pillow
```


Standard libraries like `random`, `tkinter`, and `os` are included with Python.

---

## ▶️ How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/ShakalBhau0001/Hangman-Game-GUI.git
```

**2. Enter the project folder:**

```bash
cd Hangman-Game-GUI
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Run the game:**

```bash
python main.py
```

---

## 🎯 How to Play

1. **Select a category** – choose from the sidebar: Animals, Countries, Movies, or Technology
2. **Start guessing** – click on letters from the on-screen keyboard or use your physical keyboard
3. **Use hints** – click the hint button if you need a clue
4. **Win or lose** – guess all letters correctly to win; each wrong guess adds a part to the hangman
5. **Track your score** – your wins and losses are displayed in real-time
6. **Play again** – start a new game with the same category or switch to another

---

## ⚙️ How It Works

1️⃣ Game Initialization

- Random word selected from chosen category
- Hangman drawing reset to empty state
- Game state variables (guessed letters, remaining attempts) initialized

2️⃣ Guess Processing

- Letter guess validated (not guessed before, alphabetic)
- If correct → reveal letter positions in word
- If incorrect → decrement remaining attempts, update hangman drawing

3️⃣ Win/Loss Detection

- **Win**: all letters in word guessed correctly
- **Loss**: remaining attempts reach zero (hangman fully drawn)

4️⃣ Scoring System

- Wins incremented on successful guesses
- Losses incremented when game ends without completion

---

## 🎨 Customization

### Adding New Word Categories

1. Open `data/words.py`
2. Add a new category dictionary with your word list:

```python
   "New Category": ["word1", "word2", "word3"]
```

3. The category will automatically appear in the sidebar


---

## 🌟 Future Enhancements

- Sound effects for correct/incorrect guesses
- Difficulty levels (word length variations)
- Multiplayer mode
- Word definitions on reveal
- Timer mode for timed challenges
- Statistics dashboard with historical scores

---

## ⚠️ Disclaimer

This project is developed for **educational purposes** to demonstrate Python GUI programming with CustomTkinter. It showcases game state management, event handling, and modern UI design principles.

---

## 🪪 Author

> **Creator: Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---
