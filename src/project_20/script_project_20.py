"""
Element Search
--------------
A CLI app that runs binary search on a list of integers to find where a user submited number fits.
"""

# Imports
import bisect, random
from collections import deque


# Input:
#   sanitize
def sanitize_input(raw: str) -> str:
    """Sanitizes user input by stripping whitespace and removing spaces."""
    return raw.strip().replace(" ", "")


#   validate
def validate_input(user_input: str) -> bool:
    """Validates that the user input is an integer between 1 and 100."""
    try:
        user_int = int(user_input)
        return 1 <= user_int <= 100
    except ValueError:
        return False


# Process:
#   Generate random list
def gen_num_list(length: int = 10) -> list[int]:
    """Generates a sorted list of unique random integers between 1 and 100."""
    num_list = random.sample(range(1, 101), length)
    num_list.sort()
    return num_list


#   Run binary search
def binary_search(arr: list[int], target: int) -> int:
    """Performs binary search to find the index where the target should be inserted."""
    # Find insert position left
    return bisect.bisect_left(arr, target)


# Modify list
def modify_list(arr: list[int], target: int, index: int) -> list[int]:
    """Inserts the target into the list at the specified index and returns the modified list."""

    dq = deque(arr)
    dq.rotate(-index)  # Rotate left
    dq.appendleft(target)
    dq.rotate(index)  # Rotate right

    return list(dq)


# Output:
#   Intro
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
    msg = "A CLI app that runs binary search on a list of integers to find where a user submited number fits."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}" + "\n"


#   Display results
def display_results(arr: list[int], index: int, modified_list: list[int]) -> str:
    """Formats the original list, the location of the target, and the modified list into a string."""
    left = arr[:index]
    right = arr[index:]
    gen_str = f"Original String: {arr}"
    insert_str = f"\nLocation: {left} ^ {right}"
    modified_str = f"\nModified List: {modified_list}"
    return gen_str + insert_str + modified_str


# Run program
def main() -> None:
    print(logo())
    while True:
        raw = input("Enter a number (1-100): ")
        user_input = sanitize_input(raw)
        if not validate_input(user_input):
            print(f"Invalid Input: {raw}")
            continue
        target = int(user_input)
        arr = gen_num_list()
        index = binary_search(arr, target)
        modified_list = modify_list(arr, target, index)

        print(display_results(arr, index, modified_list))
        break


if __name__ == "__main__":
    main()
