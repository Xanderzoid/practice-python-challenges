![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Divisor Calculator (Divisors Utility)

A CLI utility designed to calculate and display all divisors of a user-defined integer.

### 1. Description
This tool prompts the user for a number, validates the input range, and identifies all positive integers that divide the input without leaving a remainder.

#### Design Principles
- **Unix Philosophy**: Each function is isolated to a single responsibility (e.g., input validation, divisor calculation, and message formatting).
- **Complexity Analysis**: 
  - **Time Complexity**: The operation has a time complexity of $O(n)$, where $n$ is the value of the input number, as it checks all integers from 1 up to $n$.
  - **Space Complexity**: The memory scales as $O(d)$, where $d$ is the number of divisors.

### 2. Installation & Usage

1. **Requirement**: 
    - Python 3.6+
    - Standard Library (No external dependencies)

2. **Example Interaction**:
    ```text
    =======================
    B L X   D A T A M I N E
    =======================
         [Est. 2026]

    This CLI app that takes a number from a user then prints all divisors of that number.
    --------------------------------------------------------------------------------------
    Enter a number: 20
    The number 20 has 6 divisor/s they are [1, 2, 4, 5, 10, 20].
    ```

### 3. Computational Logic
The divisor logic is defined by the following set notation:
$D = \{ x \in \{1, \dots, n\} \mid n \pmod x = 0 \}$

- **$D$**: The resulting list containing the divisors.
- **$n$**: The user-defined integer input.
- **$x$**: An individual integer element within the range.

If an element $x$ divides $n$ with no remainder, it is included in the final output; otherwise, it is ignored.