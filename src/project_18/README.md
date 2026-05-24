# MIT License Notice
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
# Copyright (c) 2026 BLX Data.Mine
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files...

## Cow and Bull Game (Combinatorial State Matcher)

A lightweight CLI execution utility designed to coordinate an interactive game state engine, perform unique random sequence permutations, and cross-evaluate user multi-index strings against a hidden array target without performance degeneration.

### 1. Description
This application handles the core operational lifecycle of the classic combinatorial cryptographic codebreaking puzzle "Cows and Bulls". The platform dynamically generates non-repeating digit permutations, processes asynchronous terminal user inputs, routes system control operations, and evaluates exact positional vs. value matching metrics while maintaining linear processing metrics.

#### Design Principles
- **Unix Philosophy**: The code architecture divides runtime requirements into atomic functional barriers. Interface parsing, sequence generation, mathematical string variance calculation, and command processing operations are isolated within individual pure execution utilities (`sanitize_input`, `four_digit_number`, `number_variance`, and `user_commands`), maximizing overall modularity.
- **Predictable State**: The script separates display layers from core logical layers. Game structures evaluate state metrics deterministically, accepting data vectors from the CLI input loop and returning localized calculation dictionaries without modifying or leaking state boundaries.
- **Complexity Analysis**:
  - **Time Complexity**: $\mathcal{O}(N)$ linear time complexity. Comparing user guesses against the hidden combination target parses the character array length ($N=4$) in exactly one linear iteration. Sub-scan elements utilize set-based hash containers to maintain sub-checks at an optimal $\mathcal{O}(1)$ runtime tier.
  - **Space Complexity**: $\mathcal{O}(N)$ linear space complexity. Memory footprint allocations remain bounded and restricted strictly to structural hash set generation for the target characters and local output arrays mapping match parameters.

### 2. Installation & Usage

1. **Requirements**:
    - **Python 3.11+** (Utilizes standard library utilities, random index masks, and clean type-hint declarations).
    - No external dependency packaging is required (Relies completely on native modules like `random`).

2. **Usage**:
    Spin up the execution runtime loop directly within your shell workspace:
    ```bash
    python script_project_18.py
    ```

### 3. Computational Logic
The comparative state engine classifies digit positions by mapping intersection parameters across separate user guess vectors and randomized system targets:

$$	ext{Match}(u, g) = \{ b \in 	ext{Bulls} \mid u_i = g_i \} \cup \{ c \in 	ext{Cows} \mid u_i 
eq g_i \land u_i \in S_g \}$$

#### Equation Term Definitions:
- $	ext{Match}(u, g)$: The complete mathematical multi-set evaluation checking guess values against solution blocks.
- $u$: The tokenized string sequence capturing the incoming cleaned user guess array.
- $g$: The hidden structural target string generated sequentially as the answer block.
- $i$: The specific discrete index coordinate pointer tracking sequence spaces ($i \in \{0, 1, 2, 3\}$).
- $u_i, g_i$: Subscripts denoting individual unique text characters tracked at coordinate space $i$ within their respective vectors.
- $	ext{Bulls}$: The structural evaluation pool representing an exact value match occurring precisely at an identical index.
- $	ext{Cows}$: The structural evaluation pool tracking value presence intersecting the alternative sequence elsewhere.
- $S_g$: The high-efficiency hash set look-up pool ($	ext{Set}(g)$) built natively from the generated solution string to compress lookups.

#### Performance and Security Boundaries
In digital execution loops processing sequence arrays, structural input verification and sequence space constraints conform to localized mathematical bounds. Because array mutation operations (such as `list.pop()`) are sequentially executed inside a generation routine to extract non-repeating character entries, selection tracking presents an item rearrangement layer.

While modifying raw list lengths inside runtime iterations is traditionally a **computationally intensive task** on extensive datasets due to leftward index shifting penalties ($\mathcal{O}(N)$ per pop index operation), the application introduces safety boundaries. By enforcing strict string length limits ($N=4$) via deterministic validator loops (`validate_input`) and stripping outlier conditions (such as dropping `"0"` entirely due to logical system bugs), the platform prevents memory explosion boundaries and isolates evaluation runtime safely within a tiny microsecond tier.