"""
List Overlap
------------
A CLI utility to find the overlaping numbers in two randomly generated lists.
"""

import random

# Global variables
REF_LIST_LENGTH = 10
REF_RANDOM_MAX = 20


# Intro and logo
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
    msg = "This CLI app finds the overlaping numbers in two randomly generated lists."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


# Generate random list ints (1-20)
def gen_num_list() -> list:
    gen_list = [random.randint(1, REF_RANDOM_MAX) for _ in range(REF_LIST_LENGTH)]
    gen_list.sort()
    return gen_list


# Compute intersection of two lists of ints
def list_intersect(a_list: list, b_list: list) -> list:
    a_set = set(a_list)
    b_set = set(b_list)
    inter_set = a_set & b_set
    inter_list = list(inter_set)
    inter_list.sort()
    return inter_list


# Validate user input and Regenerate/End Program controls
def validate_input():
    msg = 'Press "Enter" or "r" to regenerate and "q" to quit: '
    while True:
        raw_input = input(msg).replace(" ", "")

        user_control = raw_input.lower()
        if user_control == "r" or user_control == "":
            dataset = generate_dataset()
            print(display_dataset(dataset))
        elif user_control == "q":
            print("Ending program...")
            return
        else:
            print(f'\nInvalid characters "{raw_input}".')


# Generate two random int list and one intersection list
def generate_dataset() -> dict:
    a_list = gen_num_list()
    b_list = gen_num_list()
    inter_list = list_intersect(a_list, b_list)
    dataset = {"a_list": a_list, "b_list": b_list, "inter_list": inter_list}
    return dataset


# Display all lists
def display_dataset(dataset: dict) -> str:
    msg = f"\n1st List: {dataset['a_list']}\n2nd List: {dataset['b_list']}\nList Intersection: {dataset['inter_list']}\n"
    return msg


# Run program
def run_app() -> None:
    # Introduction
    print(intro_msg())

    # Initial dataset
    dataset = generate_dataset()
    print(display_dataset(dataset))

    # Regenerate dataset or quit
    validate_input()


if __name__ == "__main__":
    run_app()
