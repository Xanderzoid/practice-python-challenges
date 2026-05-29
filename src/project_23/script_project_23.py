"""
File Over View
--------------
A CLI app that finds overlaping numbers in two lists of prime numbers and happy numbers starting from 1 to 1000.
"""

# Global Constants
PRIMEPATH = "./data/primenumbers.txt"
HAPPYPATH = "./data/happynumbers.txt"


# Input:
#   Validate input
def validate_input(user_input: str) -> str:
    """Validates user input as either 'y' or 'q' or 'invalid'."""
    if user_input in ["y", "yes", "start", ""]:
        return "y"
    elif user_input in ["n", "no", "q", "quit"]:
        return "q"
    else:
        return "invalid"


#   Sanatize input
def sanitize_input(raw: str) -> str:
    """Removes leading and trailing whitespace."""
    return raw.strip()


# Process:
#   Read data file
def read_file(filepath: str) -> set[int]:
    """Reads data from file and returns a set of integers."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return set(map(int, file.readlines()))
    except (OSError, ValueError):
        return set()


#   Find overlapping numbers
def find_overlapping_numbers(
    prime_numbers: set[int], happy_numbers: set[int]
) -> list[int]:
    """Returns overlaping numbers."""
    collision = []
    for prime in prime_numbers:
        if prime in happy_numbers:
            collision.append(prime)
    collision.sort()
    return collision


# Output:
#   Display overlaping numbers
def display_overlapping_numbers(numbers: list[int]) -> str:
    """Displays overlaping numbers."""
    return f"The overlaping numbers are {numbers}"


#   Intro
def logo() -> str:
    """Returns BLX Data.Mine logo."""
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
    msg = "A CLI app that finds overlaping numbers in two lists of prime numbers and happy numbers starting from 1 to 1000."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}" + "\n"


# Run program
def main() -> None:
    print(logo())
    while True:
        raw = input("Enter 'y' to start or 'q' to quit: ")
        user_input = sanitize_input(raw)
        action = validate_input(user_input)
        if action == "q":
            print("\nEnd program...")
            break
        elif action == "invalid":
            print(f"Invalid Input: {raw}. Enter a valid option.")
            continue
        # acrion == "y"
        prime_numbers = read_file(PRIMEPATH)
        happy_numbers = read_file(HAPPYPATH)
        overlaping_numbers = find_overlapping_numbers(prime_numbers, happy_numbers)
        print(display_overlapping_numbers(overlaping_numbers))
        break


if __name__ == "__main__":
    main()
