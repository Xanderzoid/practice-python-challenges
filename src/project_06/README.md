![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Palindrome (String List Utility)

A CLI utility designed to determine the symmetry of user-provided strings through palindrome verification.

### 1. Description
This tool accepts string input, sanitizes it by normalizing casing and removing whitespace, and identifies whether the sequence is a palindrome (reads the same forwards and backwards).

#### Design Principles
- **Unix Philosophy**: Each function is decoupled to perform a single logical task (Sanitization, Reversal, Comparison, and Formatting).
- **Top-Down Design**: The architecture decomposes the high-level goal into discrete sub-problems, ensuring modularity and testability.
- **Complexity Analysis**: 
  - **Time Complexity**: The operation has a time complexity of $O(n)$, where $n$ is the number of characters in the string.
  - **Space Complexity**: The memory scales as $O(n)$ due to the creation of a reversed string copy.

### 2. Installation & Usage

1. **Requirement**: 
    - Python 3.6+
    - Standard Library (No external dependencies)

2. **Example Interaction**:
    ```text
    =========================
    B L X   D A T A . M I N E
    =========================
            [Est. 2026]

    A CLI app that determines if a users string is a palindrome or not.
    ------------------------------------------------------------------
    Please enter a string: Race car
    The string "Race car" is a palindrome.
    ```

### 3. Computational Logic
The palindrome verification logic is defined by the following boolean expression:
$P = (S_{norm} = S_{rev})$

- **$P$**: The boolean result (True if a palindrome).
- **$S_{norm}$**: The sanitized, lower-case input string where $S_{norm} = \{ c \in S \mid c \neq \text{' ' } \}$.
- **$S_{rev}$**: The reversed sequence of $S_{norm}$, where $S_{rev}[i] = S_{norm}[n-1-i]$.

- **Subscripts/Terms**:
    - $i$: The index of the character.
    - $n$: The total length of the sanitized string.

If the sanitized string is identical to its reverse, it is classified as a **Palindrome**.