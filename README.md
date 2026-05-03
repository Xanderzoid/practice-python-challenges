# Practice Python Challenge Index

### Acknowledgments & References

These coding challenges are sourced from the [Practice Python](https://www.practicepython.org/) website, which offers progressive exercises for beginners and experienced developers.

### Project Dependencies & Testing

To test and lint the projects, ensure `pytest` and `black` are installed:

## Project Overview
This repository serves as a log of my 40 Python Challenge journey. The goal is to cultivate a understanding of Pythonic principles, modular software design, and test-driven development (TDD).

### Primary Objectives
Algorithmic Proficiency: Solving 40 progressive logic challenges focusing on data structures and computational efficiency.

Unix Design Philosophy: Implementing modular code where each function performs a single, discrete task.

Complexity Analysis: Documenting the Big O complexity and performance characteristics of each solution.

## Challenges summary

This is a technical summary of the 40 coding challenges from PracticePython.org, including their functional purpose and computational complexity.

| # | Challenge | Description | Complexity |
|:--|:---|:---|:---|
| 01 | Character Input | Calculates the year a user will turn 100 based on their age. | $O(1)$ |
| 02 | Odd or Even | Determines if a number is odd, even, or a multiple of a custom divisor. | $O(1)$ |
| 03 | List Less Than Ten | Filters elements from a list based on a value threshold. | $O(n)$ |
| 04 | Divisors | Generates a list of all numbers that divide a user-provided integer evenly. | $O(n)$ |
| 05 | List Overlap | Returns a list containing only the elements common between two random lists. | $O(n + m)$ |
| 06 | String Lists | Checks if a user-provided string is a palindrome. | $O(n)$ |
| 07 | List Comprehensions | Uses a single line of Python to filter even elements from a list. | $O(n)$ |
| 08 | Rock Paper Scissors | A two-player game implementation using conditional logic. | $O(1)$ |
| 09 | Guessing Game One | A game where the computer picks a random number and provides hints. | $O(1)$ |
| 10 | List Overlap Comprehensions | Implements list overlap logic using Python comprehension syntax. | $O(n + m)$ |
| 11 | Check Primality | Determines if a number is prime by checking its divisors. | $O(\sqrt{n})$ |
| 12 | List Ends | Returns a new list containing only the first and last elements of an input. | $O(1)$ |
| 13 | Fibonacci | Generates the Fibonacci sequence up to a length specified by the user. | $O(n)$ |
| 14 | List Remove Duplicates | Removes duplicate values from a list using sets and loops. | $O(n)$ |
| 15 | Reverse Word Order | Reverses the order of words in a provided string. | $O(n)$ |
| 16 | Password Generator | Creates random passwords with symbols, numbers, and letters. | $O(L)$ |
| 17 | Decode A Web Page | Scrapes a news website for article titles. | $O(n)$ |
| 18 | Cows And Bulls | Implements logic for a 4-digit number guessing game with feedback. | $O(1)$ |
| 19 | Decode Web Page Two | Scrapes content across multiple pages and outputs to console. | $O(n)$ |
| 20 | Element Search | Checks if a number exists in a list using binary search. | $O(\log n)$ |
| 21 | Write To A File | Saves program output into a local `.txt` file. | $O(n)$ |
| 22 | Read From File | Parses a text file to count specific name or category frequencies. | $O(n)$ |
| 23 | File Overlap | Identifies overlapping integers between two separate text files. | $O(n + m)$ |
| 24 | Draw A Game Board | Uses nested loops to print a visual grid of any dimensions. | $O(n^2)$ |
| 25 | Guessing Game Two | The computer attempts to guess the user's number via binary search logic. | $O(\log n)$ |
| 26 | Check Tic Tac Toe | Logic to verify winning combinations on a 3x3 grid. | $O(1)$ |
| 27 | Tic Tac Toe Draw | Handles move placement and prevents overwriting existing tiles. | $O(1)$ |
| 28 | Max Of Three | Finds the largest of three numbers using only conditional statements. | $O(1)$ |
| 29 | Tic Tac Toe Game | A fully playable, interactive terminal game. | $O(1)$ |
| 30 | Pick Word | Randomly selects a word from a dictionary file. | $O(1)$ |
| 31 | Guess Letters | Manages user input and state for hidden word guessing. | $O(n)$ |
| 32 | Hangman | Full Hangman game with visual state and secret word logic. | $O(n)$ |
| 33 | Birthday Dictionaries | Stores and retrieves birthdays using a Python dictionary. | $O(1)$ |
| 34 | Birthday JSON | Persists birthday data using JSON files on disk. | $O(n)$ |
| 35 | Birthday Months | Counts the frequency of birth months from stored data. | $O(n)$ |
| 36 | Birthday Plots | Visualizes birth month distributions using histograms. | $O(n)$ |
| 37 | Functions Refactor | Refactors scripts to separate logic from I/O for testability. | $O(1)$ |
| 38 | f-Strings | Demonstrates modern string interpolation for clean output. | $O(1)$ |
| 39 | Character Input Datetime | Uses `datetime` for precise age-based year calculations. | $O(1)$ |
| 40 | Error Checking | Implements `try-except` blocks for robust input handling. | $O(1)$ |

## Complexity Legend
* $n$: Number of elements in the primary input.
* $m$: Number of elements in a secondary input.
* $L$: Desired length of a generated sequence.

---
*Note: Web scraping tasks (17, 19) are I/O intensive; computational complexity refers to the processing of the retrieved DOM.*
challenge_index.md
Displaying challenge_index.md.