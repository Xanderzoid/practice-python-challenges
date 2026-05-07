"""
List Comprehensions
-------------------
This CLI app extracts the even number from a randomly generated list. For the sake of learning the code is more compless than the exersise.
"""
import random

# Global Constants
MAX_INT = 100
LIST_LENGTH = 10


# Input: Generate random list
def random_list() -> list:
    """
    Returns a list of random integers.
    Time: O(n log n) due to sorting.
    Space: O(n) using list.
    """
    ran_list = [random.randint(1, MAX_INT) for _ in range(LIST_LENGTH)]
    ran_list.sort()
    return ran_list


# Process: Extract even numbers from list
def extract_even(input_list: list) -> list:
    """
    Returns a list of even numbers from a list.
    Time: O(n log n) due to sorting.
    Space: O(n) using list and sets.
    """
    unique_list = list(set(input_list))
    unique_list.sort()
    return [x for x in unique_list if x % 2 == 0]


# Output: Print list of even numbers
def intro_msg() -> str:
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
    msg = "This CLI app extracts the even number from a randomly generated list."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


def format_intro(num_list: list) -> str:
    """Returns the into message string"""
    return f"Randomly Generated List: {num_list}"


def format_result(even_list: list) -> str:
    return f"The list of even numbers are {even_list}"


def main() -> None:
    print(intro_msg())
    num_list = random_list()
    print(format_intro(num_list))
    even_list = extract_even(num_list)
    print(format_result(even_list))


if __name__ == "__main__":
    main()
