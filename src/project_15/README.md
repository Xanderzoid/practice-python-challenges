![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Word Inverter (Reverse Word Order)

A memory-efficient CLI utility designed to tokenize natural language strings and invert their word sequence while maintaining text structure and eliminating extraneous whitespace.

### 1. Description
This tool processes string inputs from a user, isolates individual word tokens, and reverses their order. It is optimized for low-latency text transformations and enforces validation boundaries to prevent memory overhead during processing.

#### Design Principles
- **Unix Philosophy**: The application is decomposed into independent functional blocks: `validate_input` for input parameter checking, `sanitize_input` for tokenization and string filtering, and `reverse_str` for the structural inversion sequence.
- **Predictable State**: The utility relies on stateless transformations. It leverages pure functions that take inputs and yield new string outputs without mutating the original input text or introducing global side effects.
- **Complexity Analysis**: 
  - **Time Complexity**: $O(n)$ linear time, where $n$ represents the number of characters in the input string. Both token splitting and structural array joining traverse the character array exactly once.
  - **Space Complexity**: $O(n)$ linear space. The tool temporarily allocates memory proportional to the length of the string to store isolated word tokens within an intermediate collection.

### 2. Installation & Usage

1. **Requirement**: 
    - **Python 3.11+** (Utilizes standard built-in type hints and optimal memory optimizations).
    - Standard Library (No external project dependencies required).

2. **Usage**:
    Run the application directly via your shell terminal:
    ```bash
    python script_project_15.py
    ```

### 3. Computational Logic
The utility evaluates and alters structural data via sequential operations:

Let $W$ represent the ordered tuple of string tokens extracted from the raw user text input $T$. The transformation mapping $R(W)$ produces the inverted sentence structure:

$$R(W) = \bigoplus_{i=1}^{k} w_{k - i + 1}$$

#### Equation Term Definitions:
- $R(W)$: The final output string with reversed word ordering.
- $W$: The sequence array holding all extracted words.
- $w$: A specific word string token within the sequence array.
- $k$: The total scalar number of words identified in the array.
- $i$: The iteration loop counter variable.
- $k - i + 1$: The descending subscript index expression used to fetch words in reverse sequential order.
- $\bigoplus$: The string concatenation operation that joins tokens using an explicit single-space delimiter.

#### Performance and Distribution
Natural language corpora heavily exhibit a power law distribution known as **Zipf's Law**. The frequency of any word token is inversely proportional to its rank in the frequency table.

The distribution can be mathematically expressed as:

$$P_r = \frac{C}{r^{\alpha}}$$

#### Zipf's Law Term Definitions:
- $P_r$: The occurrence probability or frequency of a word. The subscript $r$ denotes its positional index within the frequency ranking.
- $r$: The rank order of the word from most frequent to least frequent.
- $C$: The normalization scale constant for the dataset.
- $\alpha$: The scaling exponent power parameter, typically close to $1$.

Because linguistic data follows this heavy-tailed power law distribution, a tiny fraction of highly repetitive words (the distribution head) comprises the bulk of string lengths, while rare words compose a massive long tail. 

By enforcing a hard constraint limit of 100 characters via `validate_input`, the utility truncates potential resource exhaustion vectors, rendering downstream parsing tasks completely predictable and safe from computationally intensive text allocation bottlenecks.
