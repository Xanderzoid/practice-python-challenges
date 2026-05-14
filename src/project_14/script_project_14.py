"""
List Remove Duplicates
----------------------
A CLI app that generates a list and removes all duplicates from the list.
"""

import random
from collections.abc import Sequence

# Global Constants
LIST_LEGNTH = 10
NUM_DUPS = 3


# Input:
def validate_input(raw_val: str) -> str:
    cleaned_val = raw_val.lower().replace(" ", "")
    if cleaned_val in ["y", "yes", "start", ""]:
        return "y"
    elif cleaned_val in ["no", "n", "q", "quit"]:
        return "q"
    else:
        raise ValueError(f"Invalid Input {raw_val}:")


# Process:
# Generate list with duplicates


def gen_dup_list(length: int = 10, num_dupes: int = 3) -> list[int]:
    """
    Generates a list of 'n' number random integers (1-100) with 'd' amount of repeated numbers.
    Time O(n) | Space O(n+d)
    """
    # Generate list no dupes
    unique_nums: set[int] = set()
    while len(unique_nums) < length:
        unique_nums.add(random.randint(1, 100))
    result = list(unique_nums)

    # Generate dupes
    dupes = random.choices(result, k=num_dupes)

    return result + dupes


# Remove duplicates
def remove_dup(data: Sequence[int]) -> list[int]:
    """
    Remove duplicates integers from 'n' number of elements in a list.
    Time: O(n) | Space O(n)
    """
    return list(set(data))


# Output:
# Display Intro
def logo() -> str:
    """Displays BLX Data.Mine logo."""
    ascii_art = """                 
                 ###                                       
                ##  #                                      
               ## ####                                     
              ##  #   #             =========================
             ## #### ###            B L X   D A T A . M I N E
            ##  #    #  #           =========================
           ## ####  ######                 [Est. 2026]       
          ##  #   ###     #                                
         ## #### ##  ##  ###                                """
    msg = "A CLI app that generates a list and removes all duplicates from the list."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


# Display Results
def display_results(dup_list: list[int], cleaned_list: list[int]) -> str:
    """Returns a results of ordered duplicate and cleaned lists."""
    return (
        f"The list with duplicates: {sorted(dup_list)}\n"
        f"The list without duplicates: {sorted(cleaned_list)}"
    )


# Run program
def main() -> None:
    print(logo())
    while True:
        raw = input("Enter 'y' to start or 'q' to quit: ")
        user_input = validate_input(raw)
        if user_input == "y":
            dup_list = gen_dup_list(LIST_LEGNTH, NUM_DUPS)
            cleaned_list = remove_dup(dup_list)
            print(display_results(dup_list, cleaned_list))
            continue
        else:
            print("End program...")
            break


if __name__ == "__main__":
    main()
