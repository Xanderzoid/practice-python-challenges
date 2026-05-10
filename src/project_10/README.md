![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Dice Analytics (Probability Distribution Utility)

A CLI-based statistical utility that simulates multiple dice configurations (4D3, 2D6, 1D12) to analyze outcome distributions and central tendencies.

### 1. Description
This tool executes a large-scale simulation of three distinct dice sets. It calculates the mean, identifies extreme outliers (min/max), and visualizes the relative probabilities of each outcome to demonstrate the differences between uniform and normal distributions.

#### Design Principles
- **Unix Philosophy**: The system is modularized into discrete functional units. `roll_any_die` manages simulation, while `avg_dataset` and `min_max_dataset` handle the mathematical analysis.
- **Top-Down Design**: The script utilizes a layered architecture where a high-level simulation runner orchestrates specialized statistical helpers.
- **Complexity Analysis**: 
  - **Time Complexity**: The simulation runs in $O(D \cdot X \cdot N)$, where $D$ is the number of dice sets, $X$ is the dataset size, and $N$ is the number of dice per roll. Statistical analysis is $O(n)$ relative to the number of possible outcomes.
  - **Space Complexity**: $O(V)$ auxiliary space, where $V$ is the range of possible outcomes (the number of keys in the distribution dictionary).

### 2. Installation & Usage

1. **Requirement**: 
    - Python 3.6+
    - Standard Library (No external dependencies)

2. **Usage**:
    Run the script directly via the Python interpreter:
    ```text
    python script_project_10.py
    ```

3. **Example Interaction**:
    ```text
    =========================
    B L X   D A T A . M I N E
    =========================
            [Est. 2026]

    A CLI app that randomly rolls 4 1D3, 2 1D6, and 1 1d12 100 times.
    -----------------------------------------------------------------
    4D3  AVG: 8.14 MIN: [{'4': 1}] MAX: [{'12': 2}]
    2D6  AVG: 7.02 MIN: [{'2': 3}] MAX: [{'12': 2}]
    1D12 AVG: 6.45 MIN: [{'1': 6}] MAX: [{'12': 8}]
    ```

### 3. Computational Logic
The average outcome $E[X]$ is derived from the discrete probability distribution generated during the simulation:

$E[X] = \sum_{i=1}^{n} x_i \cdot \frac{f(x_i)}{N}$

- **$x_i$**: The outcome value (e.g., a roll result of 7).
- **$f(x_i)$**: The frequency of that outcome within the dataset.
- **$N$**: The total number of rolls in the simulation.

The project demonstrates the **Central Limit Theorem**, as the 4D3 and 2D6 distributions converge toward a normal bell curve while the 1D12 distribution remains approximately uniform.