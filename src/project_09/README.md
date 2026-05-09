![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Oracle Guess (Guessing Game Utility)

A CLI-based numerical discovery utility that implements a state-managed guessing game with directional feedback and scoring persistence.

### 1. Description
This tool generates a hidden integer between 1 and 9. Through a continuous feedback loop, the user is guided toward the correct value via "too high" or "too low" indicators. The system tracks total games played and the user's success rate.

#### Design Principles
- **Unix Philosophy**: Functional responsibilities are decoupled. `validate_input` handles sanitization, `compare_num` performs the logic check, and `update_score` manages the state transition.
- **Top-Down Design**: The application utilizes a centralized `game_logic` orchestrator to manage the control flow, ensuring that UI updates and logical computations remain distinct.
- **Complexity Analysis**: 
  - **Time Complexity**: The logical comparisons and score updates occur in $O(1)$ constant time. Input validation scales at $O(n)$ relative to the length of the user's string input.
  - **Space Complexity**: $O(1)$ auxiliary space, as the application maintains a fixed number of integer variables regardless of session length.

### 2. Installation & Usage

1. **Requirement**: 
    - Python 3.6+
    - Standard Library (No external dependencies)

2. **Usage**:
    Run the script directly via the Python interpreter:
    ```text
    python script_project_09.py
    ```

3. **Example Interaction**:
    ```text
    =========================
    B L X   D A T A . M I N E
    =========================
            [Est. 2026]

    This CLI app that generates a random number between (1-9) the user must guess.
    ---------------------------------------------------------------------------
    Number of games played: 0 Player's score: 0
    Enter you guess: 5
    You're number (5) is too low, Try again.
    Number of games played: 1 Player's score: 0
    ```

### 3. Computational Logic
The game serves as a practical implementation of directional searching. By providing feedback on the relationship between the guess $g$ and the target $x$, the system reduces the search space $S$ iteratively:

$S_{next} = 
\begin{cases} 
\{i \in S \mid i > g\} & \text{if } g < x \\
\{i \in S \mid i < g\} & \text{if } g > x \\
\emptyset & \text{if } g = x 
\end{cases}$

- **$g$**: The user's current guess.
- **$x$**: The computer's randomly generated target integer.
- **$S$**: The set of possible integers $\{1, 2, \dots, 9\}$.

This feedback loop allows the user to converge on the target in a maximum of $\lceil \log_2(9) \rceil = 4$ attempts using an optimal binary search strategy.