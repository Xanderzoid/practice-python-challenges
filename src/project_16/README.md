![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Entropy Vault (Password Generator)

A secure, modular CLI utility designed to generate ASCII passwords of variable structural strength and compute their cryptographic information entropy bits.

### 1. Description
This tool generates randomized passwords based on two distinct security profiles: a high-entropy cryptographically varied configuration and a low-stakes structured multi-word configuration. It evaluates the strength of the generated sequences using Shannon entropy formulas to assess resistance against brute-force tracking metrics.

#### Design Principles
- **Unix Philosophy**: The utility is segmented into discrete, specialized modules: `sanitize_input` and `sanitize_type` for cleansing entry records, `strong_pass` and `weak_pass` for core sequence production, `analysis_entropy` for pure mathematical tracking, and `main` as the interface driver.
- **Predictable State**: The core entropy computation and string generation modules are decoupled from the execution loops, accepting parameters and returning clean dictionaries without introducing global context mutations or mutating objects in place.
- **Complexity Analysis**:
  - **Time Complexity**: $O(L)$ linear time for password generation, where $L$ represents the targeted character length of the string. 
  - **Space Complexity**: $O(L)$ linear space to allocate memory for the individual character tokens within the intermediate storage structures before compilation.

### 2. Installation & Usage

1. **Requirement**:
    - **Python 3.11+** (Leverages built-in typing syntax and modern mathematical interpreter frameworks).
    - Standard Library (Zero third-party package allocations required).

2. **Usage**:
    Launch the interactive interface via your terminal prompt:
    ```bash
    python script_project_16.py
    ```

### 3. Computational Logic
The application establishes password security measurements using fundamental algebraic properties of combinations and information theory:

The total unique combination space ($N$) for an ideal randomly selected password is calculated exponentially as:

$$N = R^L$$

#### Equation Term Definitions:
- $N$: The total scalar number of unique permutations within the cryptographic search space.
- $R$: The base cardinality representing the pool size of unique available characters.
- $L$: The structural length exponent representing total characters in the password sequence.

The information entropy ($E$), quantifying the mathematical uncertainty in bits, is mapped via the base-2 logarithm of the combination space:

$$E = \log_2(N) = L \cdot \log_2(R)$$

#### Equation Term Definitions:
- $E$: The final information entropy metric expressed in bits.
- $L$: The linear multiplier coefficient representing password character length.
- $\log_2$: The binary logarithmic base operator used to scale geometric search spaces into bits [cite: 2025-12-01].
- $R$: The operand mapping the alphabet pool size ($STRONG\_UNI = 87$ or $WEAK\_UNI = 26$).

#### Performance and Security Boundaries
While password generation is exceptionally fast and lightweight, exhaustively traversing the search space during a keyspace audit represents an incredibly **computationally intensive task** for an external system. As length increases linearly, the complexity scales exponentially at $O(R^L)$, shifting security thresholds from vulnerable to mathematically unfeasible.
