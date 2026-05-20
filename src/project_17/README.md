![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Web Page Decoder (NYT Headline Extractor)

A memory-efficient CLI utility designed to perform structured remote network requests, parse DOM structures, and isolate unique article titles from live web environments without excessive computational memory overhead.

### 1. Description
This tool automates HTTP text queries targeting the remote homepage of *The New York Times*. It handles raw network byte-streams, builds hierarchical object representations using target components, and strips matching tag hierarchies down to clean text sequences while enforcing strict local deduplication barriers.

#### Design Principles
- **Unix Philosophy**: The implementation separates operational requirements into discrete functional structures [cite: 2025-11-30]. Interface validation, remote payload collection, and parsing routines are handled by specialized methods (`validate_input`, `url_scrapper`, and `extract_articles_title`), maximizing atomic reusability.
- **Predictable State**: The architecture prioritizes stateless operations. The parsing logic operates as a pure data pipeline, accepting structured document objects and returning isolated collections without introducing side effects or mutating historical inputs.
- **Complexity Analysis**:
  - **Time Complexity**: $\mathcal{O}(N)$ linear time complexity [cite: 2026-04-13]. The engine processes the document content by executing a single linear pass over the element collection to filter the target structures.
  - **Space Complexity**: $\mathcal{O}(U)$ linear auxiliary space complexity [cite: 2026-04-13]. Storage scales proportionally to the number of unique article string elements ($U$) retained inside the tracking set to guarantee absolute local deduplication.

### 2. Installation & Usage

1. **Requirements**:
    - **Python 3.11+** (Leverages advanced type-hinting annotations and modern language features).
    - `requests` (For network request transport abstraction).
    - `beautifulsoup4` (For building structural document parse trees).

2. **Usage**:
    Execute the orchestrator directly from your terminal session:
    ```bash
    python script_project_17.py
    ```

### 3. Computational Logic
The parsing architecture extracts target strings by detecting clean structural anchor hierarchies within the HTML DOM framework:

$$\text{Target} = \{ t \mid \exists p \in \text{DOM}_{\text{p}}, \, \text{Parent}(p) \in \text{DOM}_{\text{div}} \land \text{Parent}(\text{Parent}(p)) \in \text{DOM}_{\text{a}} \}$$

#### Equation Term Definitions:
- $\text{Target}$: The final collection of extracted textual titles isolated for clean terminal display.
- $t$: A clean, stripped string sequence representing an individual unique headline.
- $p$: An individual HTML paragraph element node queried within the DOM tree loop.
- $\text{DOM}_{\text{p}}$: The comprehensive structural pool of all paragraph (`<p>`) tags found across the source document.
- $\text{DOM}_{\text{div}}$: The element type classification representing block layout container tags (`<div>`).
- $\text{DOM}_{\text{a}}$: The structural group mapping hypertext anchor links (`<a>`) containing resource navigation components.

#### Performance and Security Boundaries
In live digital networking environments, live page payload lengths often follow a **Power Law Distribution**, where a small subset of headline elements clusters heavily across high-frequency front pages, while deep-link text nodes create a vast, unpredictable long tail of markup bytes
Because downloading and processing heavy web documents represents an incredibly **computationally intensive task**, the application introduces strict networking safety guards. By applying explicit network timeout values ($\text{timeout}=10$) and throwing structural exceptions (`RequestException`) during connection breakdowns, the engine stops resource exhaustion blocks, making downstream processing safe from memory leak vectors.