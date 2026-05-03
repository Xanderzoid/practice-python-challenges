![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Threshold Filter (List Less Than Ten Utility)

A CLI utility designed to filter numerical sequences based on a user-defined threshold.

### 1. Description
This tool processes a predefined list of numbers and extracts all elements that are strictly less than a value provided by the user.

#### Design Principles
- **Unix Philosophy**: Each function is isolated to a single responsibility (e.g., input validation, list computation, and message formatting).
- **Complexity Analysis**: The filtering process involves a single pass through the input list, resulting in a time complexity of $O(n)$, where $n$ is the number of elements in the reference list.


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

    This CLI app displays all numbers within a list less than your number.
    ----------------------------------------------------------------------
    Number List: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    Enter your number: 5
    List of numbers less than 5: [1, 1, 2, 3]
    ```

### 3. Computational Logic
The filtering logic is defined by the following set notation:
$L_{res} = \{ x \in L_{ref} \mid x < n \}$

- **$L_{res}$**: The resulting list containing the filtered elements.
- **$L_{ref}$**: The reference list of numbers to be evaluated.
- **$x$**: An individual element within the reference list.
- **$n$**: The threshold value provided by the user.

If an element $x$ satisfies the condition of being less than $n$, it is included in the final output; otherwise, it is ignored.