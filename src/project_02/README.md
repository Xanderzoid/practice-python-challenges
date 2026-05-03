![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Parity Detective (Odd or Even Utility)

A precision CLI utility designed to determine the parity of user-provided numerical data.

### 1. Description
This tool accepts numerical input from a user and identifies whether the value is **Odd** or **Even**.

#### Design Principles
- **Unix Philosophy**: Each function is decoupled to perform a single logical task (Input Validation, Parity Identification, Message Formatting).
- **Complexity Analysis**: The core logic uses the modulo operator, achieving a time complexity of $O(1)$. 


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

    This CLI app checks if a user's number is odd or even.
    ----------------------------------------------------
    Enter your number: 42
    The number 42.0 is even.
    ```

### 3. Computational Logic
The parity is determined using the following equation:
$R = n \pmod 2$

- **$R$**: The remainder of the division.
- **$n$**: The user-provided numerical input.
- **$\pmod$**: The modulo operator, which returns the remainder after division.

If $R = 0$, the number is classified as **Even**. Otherwise, it is **Odd**.