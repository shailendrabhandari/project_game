# ACIT_GAME_Module

**ACIT_GAME_Module** is a fun and educational Python game package developed as part of the ACIT4420 lecture series. The package includes three classic games: Rock, Paper, Scissors; Guess the Number; and Tic-Tac-Toe. This project demonstrates fundamental Python programming concepts, including module organization, package management, and user interaction through command-line interfaces.
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Games Included](#games-included)
- [Project Structure](#project-structure)
- [License](#license)
## Features
- Three classic games: Rock, Paper, Scissors; Guess the Number; and Tic-Tac-Toe.
- Easy to install and run using a command-line interface.
- Educational for those learning Python and package management.
- Modular design for easy extension and maintenance.
## Installation
To get started, follow these steps:
1. **Clone the Repository** (or download the package):
   ```bash
   git clone https://github.com/your-username/ACIT_GAME_Module.git
   cd ACIT_GAME_Module
   ```
2. **Create a Virtual Environment** (recommended):
   ```bash
   python3 -m venv gameenv
   source gameenv/bin/activate  # On Windows, use `gameenv\Scripts\activate`
   ```
3. **Install the Package**:
   ```bash
   pip install -e .
   ```
## Usage
Once installed, you can play the games by running the following command in your terminal:
```bash
games
```
This will launch a menu where you can choose between the three available games:
1. **Rock, Paper, Scissors**
2. **Guess the Number**
3. **Tic-Tac-Toe**
Simply enter the number corresponding to the game you want to play, and follow the on-screen instructions.
## Games Included
### 1. Rock, Paper, Scissors
A simple implementation of the classic hand game. Choose Rock, Paper, or Scissors, and see if you can beat the computer.
### 2. Guess the Number
The computer randomly selects a number between 1 and 10. Your goal is to guess the number in as few attempts as possible.
### 3. Tic-Tac-Toe
A digital version of the classic two-player game. Play against the computer and try to get three in a row.
## Project Structure
Here is a brief overview of the project's structure:
```
ACIT_GAME_Module/
│
├── games/
│   ├── __init__.py
│   ├── main.py                # Entry point for the game menu
│   ├── rock_paper_scissor/
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   └── game_logic.py
│   ├── guess_the_number.py
│   └── tic_tac_toe.py
│
├── setup.py                   # Installation script
└── README.md                  # Project documentation (this file)
```
### Key Files:
- **`main.py`**: Contains the main function that launches the game menu.
- **`setup.py`**: Script for installing the package.
- **`rock_paper_scissor/`**: Submodule containing logic for the Rock, Paper, Scissors game.
- **`guess_the_number.py`**: Script for the Guess the Number game.
- **`tic_tac_toe.py`**: Script for the Tic-Tac-Toe game.
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
