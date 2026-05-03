![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## List Overlap Utility

A CLI utility designed to generate and compare random numerical sets to find overlapping values.

### 1. Description
This tool generates two random lists of integers, sorts them, and computes the intersection (common elements) between the two sequences.

#### Design Principles
- **Unix Philosophy**: Each function is isolated to a single responsibility (e.g., random generation, set intersection computation, and data formatting).
- **Complexity Analysis**: 
  - **Time Complexity**: The operation has a time complexity of $O(n + m)$, where $n$ and $m$ are the lengths of the respective lists, determined by set intersections. Sorting lists takes $O(n \log n)$ time.
  - **Space Complexity**: The memory scales as $O(k)$, where $k$ is the number of overlapping elements.

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

    This CLI app finds the overlaping numbers in two randomly generated lists.
    ----------------------------------------------------------------------
    1st List: [2, 4, 6, 8, 11, 13, 14, 16, 17, 19]
    2nd List: [1, 5, 8, 10, 11, 14, 16, 17, 18, 20]
    List Intersection: [8, 11, 14, 16, 17]

    Press "Enter" or "r" to regenerate and "q" to quit: 
    ```

### 3. Computational Logic
The set intersection logic is defined by the following set notation:
$I = \{ x \mid x \in A \land x \in B \}$

- **$I$**: The resulting list containing the intersecting elements.
- **$A$**: The first randomly generated list.
- **$B$**: The second randomly generated list.
- **$x$**: An individual integer element within the sequence.

If an element $x$ exists in both set $A$ and set $B$, it is included in the final output intersection; otherwise, it is excluded.