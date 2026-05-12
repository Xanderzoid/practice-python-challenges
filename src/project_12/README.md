![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Boundary Extractor (List Ends Utility)

A CLI-based data transformation utility that generates random numerical sequences and extracts their boundary elements (first and last) into a specialized subset.

### 1. Description
This tool automates the creation of a 10-integer dataset and isolates the terminal points of the list. It features a command-normalization engine that accepts various natural language prompts for control flow.

#### Design Principles
- **Unix Philosophy**: Responsibilities are strictly partitioned. `generate_list` handles data creation, `remove_first_last` handles logical extraction, and `validate_input` manages interface normalization.
- **Top-Down Design**: The application logic flows from a high-level `main()` loop down to $O(1)$ primitive operations, ensuring the orchestrator remains decoupled from the data processing logic.
- **Complexity Analysis**: 
  - **Time Complexity**: $O(1)$ constant time for the core extraction. Accessing the first (`[0]`) and last (`[-1]`) indices of a Python list is a direct memory lookup independent of list length.
  - **Space Complexity**: $O(1)$ auxiliary space. The resulting list always contains exactly two elements, regardless of the input size.

### 2. Installation & Usage

1. **Requirement**: 
    - Python 3.6+
    - Standard Library (No external dependencies)

2. **Usage**:
    Run the script directly via the Python interpreter:
    ```text
    python script_project_12.py
    ```

3. **Example Interaction**:
    ```text
    =========================
    B L X   D A T A . M I N E
    =========================
            [Est. 2026]

    A CLI app generates a list and removes the first and last elements.
    ------------------------------------------------------------------
    Enter 'y' to start or 'q' to quit: start

    The generated list: [42, 7, 19, 88, 3, 54, 91, 12, 60, 5]
    The truncated list: [42, 5]
    ```

### 3. Computational Logic
The utility performs a selection transformation on a finite sequence $A$. If $A$ is a sequence of length $n$, the result $B$ is defined by the values at the interval boundaries:

$B = (a_i, a_j) \text{ where } i = 0, j = n-1$

- **$a_0$**: The head (initial element) of the sequence.
- **$a_{n-1}$**: The tail (final element) of the sequence.
- **Indexing**: The script utilizes Python's negative indexing property where $a_{-1} \equiv a_{n-1}$, allowing for safe terminal access without explicit length calculations.

For edge cases where the sequence length $|A| < 2$, the system maintains structural integrity by duplicating the head element to fill the boundary pair.