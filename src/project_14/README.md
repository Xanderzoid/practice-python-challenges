![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## List Remove Duplicates (Duplicate Remover)

A CLI utility designed to generate randomized datasets and execute deduplication removal, ensuring data integrity for downstream processing.

### 1. Description
This tool automates the creation of a numerical dataset containing intentional redundancies and applies a set-theoretic transformation to isolate unique values. It maintains linear efficiency during both the generation and cleaning phases.

#### Design Principles
- **Unix Philosophy**: The application is decomposed into discrete functional units: `gen_dup_list` for data synthesis, `remove_dup` for logical deduplication, and `validate_input` for interface normalization.
- **Predictable State**: By utilizing `sorted()` during output generation, the utility provides a deterministic view of the processed data without mutating the original underlying sequences.
- **Complexity Analysis**: 
  - **Time Complexity**: $O(n)$ linear time. Using hash-based sets for membership checks during generation and deduplication ensures that performance scales predictably with input size.
  - **Space Complexity**: $O(n)$ linear space. The utility requires sufficient memory to store the unique elements of the set during the transformation process.

### 2. Installation & Usage

1. **Requirement**: 
    - **Python 3.11+** (Leverages modern `collections.abc` and advanced type hinting).
    - Standard Library (No external dependencies).

2. **Usage**:
    Execute the script via the terminal:
    ```bash
    python script_project_14.py
    ```

### 3. Computational Logic
The utility employs a two-stage process to manage data redundancy:

1. **Stochastic Generation**: A set-based loop ensures the creation of a unique base population, followed by a randomized selection (`random.choices`) to inject a controlled number of duplicates.
2. **Set Transformation**: The cleaning logic utilizes the properties of a hash set to perform deduplication in a single pass:
   
   $$S = \{x \mid x \in L\}$$
   
   Where $L$ is the original list and $S$ is the resulting set of unique members.

#### Performance and Distribution
Real-world datasets often exhibit a **Power Law Distribution**, where a small subset of values appears with high frequency while most values appear rarely. The use of $O(n)$ hash-based deduplication is a mechanical necessity for handling such distributions at scale, as it prevents the **computationally intensive** quadratic slowdown ($O(n^2)$) associated with nested-loop list comparisons.
