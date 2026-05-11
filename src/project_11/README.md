![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Prime Detective (Primality & Factor Utility)

A CLI utility designed to evaluate the primality of integers and perform divisor extraction for non-prime values.

### 1. Description
This tool determines whether a user-provided integer (ranging from 1 to 100) is a prime number. For composite numbers, the utility performs a full factorization to identify and display all positive divisors.

#### Design Principles
- **Unix Philosophy**: Logical tasks are decoupled into single-purpose functions. `is_prime` handles the boolean evaluation, while `find_divisors` handles data extraction for composite results.
- **Top-Down Design**: The script architecture is decomposed into distinct phases: Input Validation, Mathematical Analysis, and Dynamic String Formatting.
- **Complexity Analysis**: 
  - **Time Complexity**: 
    - `is_prime`: $O(\sqrt{n})$, achieved by terminating the search at the square root of the input.
    - `find_divisors`: $O(n)$, requiring a linear scan to identify all factors.
  - **Space Complexity**: $O(d)$, where $d$ is the number of divisors stored for output.

### 2. Installation & Usage

1. **Requirement**: 
    - Python 3.6+
    - Standard Library (No external dependencies)

2. **Usage**:
    Run the script directly via the Python interpreter:
    ```text
    python script_project_11.py
    ```

3. **Example Interaction**:
    ```text
    =========================
    B L X   D A T A . M I N E
    =========================
            [Est. 2026]

    A CLI app that ask the user for a integer and determine whether the integer is prime or not.
    ------------------------------------------------------------------------------------------
    Enter a integer between (1-100): 13
    Yes, 13 is a prime number!
    ```

### 3. Computational Logic
Primality is determined by evaluating the existence of divisors within the set of integers. The utility optimizes this search using the property that if $n$ is composite, it must have a factor less than or equal to $\sqrt{n}$.

$P(n) = 
eg \exists \ x \in \mathbb{Z} : (1 < x \leq \sqrt{n}) \land (n \pmod x = 0)$

- **$n$**: The input integer.
- **$x$**: The divisor candidate.
- **$\pmod x = 0$**: The congruence relation indicating that $x$ divides $n$ without a remainder.

For numbers failing this check, the utility identifies the set of divisors $D$:
$D = \{ d \in \mathbb{Z}^+ \mid n \pmod d = 0 \}$