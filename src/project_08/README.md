![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## RPS Duel (Rock Paper Scissors Utility)

A CLI-based game utility that implements the classic Rock Paper Scissors logic using modular functional design and robust input validation.

### 1. Description
This tool allows a user to compete against an automated computer opponent. It features a sanitized input loop that handles case-insensitive commands and provides descriptive feedback on game outcomes.

#### Design Principles
- **Unix Philosophy**: Logic is strictly partitioned. `get_hand` handles validation, `game_logic` determines the victor, and `display_result` manages the UI string construction.
- **Top-Down Design**: The application uses a high-level orchestrator (`validate_input`) to manage the program state while delegating specific computations to low-level helper functions.
- **Complexity Analysis**: 
  - **Time Complexity**: The core logic operates at $O(1)$ constant time as the decision tree does not scale with input size. Input sanitization is $O(n)$ relative to the length of the input string.
  - **Space Complexity**: $O(1)$ auxiliary space is used for game state dictionaries.

### 2. Installation & Usage

1. **Requirement**: 
    - Python 3.6+
    - Standard Library (No external dependencies)

2. **Usage**:
    Run the script directly via the Python interpreter:
    ```text
    python script_project_08.py
    ```

3. **Example Interaction**:
    ```text
    =========================
    B L X   D A T A . M I N E
    =========================
            [Est. 2026]

    This CLI plays the game rock, paper, scissors with the user.
    -----------------------------------------------------------
    Enter 'r'(Rock) or 'p'(Paper) or 's'(Scissors): r
    The computer choose Paper. Paper beats Rock. The computer won :(
    ```

### 3. Computational Logic
The game outcome $W$ is determined by evaluating the relationship between the player's choice $p$ and the computer's choice $c$. While the script uses boolean mapping, the underlying logic follows a modular arithmetic model where $R=0, P=1, S=2$:

$W = (p - c) \pmod{3}$

- **$W = 0$**: Draw (Both players selected the same hand).
- **$W = 1$**: Player Victory (e.g., Paper (1) - Rock (0) = 1).
- **$W = 2$**: Computer Victory (e.g., Rock (0) - Paper (1) = -1 $\equiv 2 \pmod{3}$).

**Subscripts/Terms**:
- $p, c$: Discrete values representing the chosen hands.
- $\pmod{3}$: The modulo operator representing the three possible states in the circular win-loss relationship.