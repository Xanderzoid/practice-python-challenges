"""
Reverse Word Order
------------------
This CLI app reverses the order of words entered from a user.
"""


# Input: validate, sanitize
def validate_input(text: str) -> bool:
    """Validates string's character size is between 1 and 100 characters."""
    return 1 <= len(text) <= 100


def sanitize_input(text: str) -> list[str]:
    """
    Extracts words from a string, automatically dropping arbitrary whitespace.
    Time: O(n) | Space O(n), where n is the number of words
    """
    return text.split()


# Process: reverse_str
# Reverse string
def reverse_str(msg: list[str]) -> str:
    """Returns a reversed order of a list of strings as a string."""
    return " ".join(reversed(msg))


# Output: intro, results
# Intro
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
    msg = "This CLI app reverses the order of words entered from a user."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


# Results
def display_results(reversed_str: str) -> str:
    """Formats output message."""
    return f"Your reversed string of words are: {reversed_str}"


# Run program:
def main() -> None:
    print(logo())
    while True:
        raw = input("Enter a string of words to revere (1-100 characters): ")
        if not validate_input(raw):
            print(f"Invalid Input {raw}: Please conform to length rules.")
            continue

        user_str = sanitize_input(raw)
        reversed_user_str = reverse_str(user_str)
        print(display_results(reversed_user_str))
        break


if __name__ == "__main__":
    main()
