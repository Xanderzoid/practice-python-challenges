![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Sequence Architect (Fibonacci Generator)

A memory-efficient CLI utility that generates mathematical sequences based on the Fibonacci recurrence relation, optimized for terminal-based data exploration.

### 1. Description
This tool computes a sequence of integers where each number is the sum of the two preceding ones. It utilizes a lazy-evaluation engine to ensure constant memory overhead even when processing the upper bounds of the allowed input range.

#### Design Principles
- **Unix Philosophy**: The utility is partitioned into atomic units: `get_fibonacci_sequence` acts as a pure data producer, `parse_and_validate` manages interface normalization, and `main` serves as the I/O orchestrator.
- **Memory Efficiency**: Unlike standard list-based approaches, the core engine uses Python **Generators**, maintaining a stateful stream of data rather than an eager collection.
- **Complexity Analysis**: 
  - **Time Complexity**: $O(n)$ linear time. The script must perform $n$ additions to reach the $n^{th}$ element in the sequence.
  - **Space Complexity**: $O(1)$ constant auxiliary space for the generator [cite: 2025-12-16]. The internal state only tracks two variables ($a$ and $b$) regardless of the requested length.

### 2. Installation & Usage

1. **Requirement**: 
    - **Python 3.11+** (Utilizes modern type hinting and `collections.abc`).
    - Standard Library (Zero external dependencies).

2. **Usage**:
    Run the script via the Python interpreter:
    ```bash
    python script_project_13.py
    ```

### 3. Computational Logic
The utility calculates the sequence $F$ based on the following mathematical recurrence:

$$F_n = F_{n-1} + F_{n-2}$$

Where the initial seeds are defined as:
- $F_0 = 1$
- $F_1 = 1$
- $n$: The user-defined sequence length, where $1 \le n \le 20$.

#### Performance and Distribution
In large-scale data environments, request lengths often follow a **Power Law Distribution**, where most users request small sequences while a few "power users" request the maximum allowed length. By enforcing a hard limit of $n=20$ and utilizing $O(1)$ space complexity, the system prevents **computationally intensive** memory allocation tasks from impacting host performance.