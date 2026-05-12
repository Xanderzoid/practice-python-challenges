"""
List Ends
---------
This CLI app generates a list and removes the first and last elements and appends them to a new list.
"""
import random

# Global Constants
LIST_LENGTH = 10


# Input:
# Start command
def validate_input(raw: str) -> str:
    """Sanitizes the generate and quit text."""
    user_input = raw.lower().replace(" ", "")
    if user_input in ["yes", "next", "start", ""]:
        user_input = "y"
    if user_input in ["quit", "exit", "end", "no"]:
        user_input = "q"
    return user_input


# Process:
# Generate list of random integers
def generate_list(length: int) -> list:
    """Returns a list of 'length' number of integers (0-100)."""
    return [random.randint(0, 100) for _ in range(length)]


# Remove first and last elements from a list
def remove_first_last(data_list: list) -> list:
    """Returns a list containg the first and last elements of the 'data_list'."""
    if len(data_list) >= 2:
        return [data_list[0], data_list[-1]]
    else:
        return [data_list[0], data_list[0]]


# Output:
# Intro text
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
    msg = "A CLI app generates a list and removes the first and last elements and appends them to a new list."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


# Display generated list and new composite list
def display_result(gen_list: list, trunk_list: list) -> str:
    """Returns generated list and truncated list message."""
    return f"\nThe generated list: {gen_list}\nThe truncated list: {trunk_list}"


# Run program
def main() -> None:
    print(logo())
    while True:
        raw = input("Enter 'y' to start or 'q' to quit: ")
        user_input = validate_input(raw)
        if user_input == "q":
            print("\nEnd program...")
            break
        elif user_input == "y":
            gen_list = generate_list(LIST_LENGTH)
            trunk_list = remove_first_last(gen_list)
            print(display_result(gen_list, trunk_list))
            continue
        else:
            print(f"Invalid input {raw}:")
            continue


if __name__ == "__main__":
    main()
