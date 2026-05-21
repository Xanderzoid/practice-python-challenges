"""
Cow and Bull Game
-----------------
A CLI app that plays the cow and bull game with the user.
The game is simple: the computer generates a random 4-digit number,
and the user has to guess it. For every guess, the computer will give
feedback in the form of "cows" and "bulls". A "cow" means that one of
the digits in the user's guess is correct but in the wrong position,
while a "bull" means that one of the digits is correct and in the
correct position. The game continues until the user guesses the
number correctly, at which point they win.
"""

import random

# Global constants
RULES = """
The game is simple: the computer generates a random 4-digit number,and the user has to guess it. 
For every guess, the computer will give feedback in the form of "cows" and "bulls". 
A "cow" means that one of the digits in the user's guess is correct but in the wrong position, while a "bull" means that one of the digits is correct and in the 
correct position. 
The game continues until the user guesses the number correctly, at which point they win.
"""


# Input:
#   Validate that the user's input is a 4-digit number.
def validate_input(user_input: str) -> bool:
    """Validates that the user's input is a 4-digit number."""
    try:
        # The number cannot contain 0, and must be 4 digits long with all digits being unique.
        user_set = set(user_input)
        if "0" in user_set:  # Allowing 0 causes too many problems
            return False
        if len(user_set) == 4 and user_input.isdigit():
            return True
        return False
    except ValueError:
        return False


def sanitize_input(raw_input: str) -> str:
    """Sanitizes the user's input by stripping whitespace and removing spaces."""
    user_input = raw_input.strip().replace(" ", "")
    return user_input


# Process:
#   Generate a random 4-digit number.
def four_digit_number() -> str:
    """Generates a random 4-digit number with unique digits from 1 to 9."""
    number_list = [x for x in range(1, 10)]
    random_list = []
    # Pop 4 unique digits from the number list and append them to the random list.
    for _ in range(4):
        random_list.append(
            str(number_list.pop(random.randint(0, len(number_list) - 1)))
        )
    return "".join(random_list)


#   Compare the user's guess with the generated number and count the cows and bulls.
def number_variance(user_str: str, gen_str: str) -> dict[str, int]:
    """Compares the user's guess with the generated number and counts the cows and bulls."""
    variance = {"cows": 0, "bulls": 0}
    # Validate_input prevents duplicate digits
    gen_set = set(gen_str)
    for index in range(4):
        if user_str[index] == gen_str[index]:
            variance["bulls"] += 1
        else:
            if user_str[index] in gen_set:
                variance["cows"] += 1
    return variance


def user_commands(user_input: str) -> dict[str, bool]:
    """Checks if the user's input is a command and executes it."""
    command_dict = {"rules": False, "quit": False, "invalid": False}
    if user_input in ["r", "rules"]:
        command_dict["rules"] = True
    elif user_input in ["q", "quit", "exit"]:
        command_dict["quit"] = True
    else:
        command_dict["invalid"] = True
    return command_dict


# Output:
#   Introduce the game and explain the rules to the user.
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
    msg = "A CLI app that plays the cow and bull game with the user."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


#   Display the number of cows and bulls to the user after each guess.
def display_results(variance: dict[str, int]) -> str:
    """Displays the number of cows and bulls to the user after each guess."""
    return f"{variance["cows"]} cows, {variance["bulls"]} bulls"


# Run program
def main() -> None:
    print(logo())
    gen_number = four_digit_number()
    attempts = 1
    while True:
        # Get input from user
        raw = input("Enter a 4 digit number (1-9) or 'r' for rules or 'q' to quit: ")
        user_number = sanitize_input(raw)
        # Validate input
        if not validate_input(user_number):
            command_dict = user_commands(user_number)
            if command_dict["rules"]:
                print(RULES)
                continue
            elif command_dict["quit"]:
                print("Thanks for playing! Goodbye!")
                break
            elif command_dict["invalid"]:
                print(f"Invalid input {raw}, please try again.")
                continue

        # Compute and display results
        variance = number_variance(user_number, gen_number)
        print(display_results(variance))
        if variance["bulls"] == 4:
            print(f"You won!, with {attempts} number of attempts.")
            break
        # Keep score
        attempts += 1


if __name__ == "__main__":
    main()
