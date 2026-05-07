"""
String List
-----------
A CLI app that determines if a user's string is a palindrome or not.
"""
# Global Constant
PROMPT_MSG = "Please enter a string: "


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
    msg = "A CLI app that determines if a user's string is a palindrome or not."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


def validate_input(user_input) -> str:
    """
    Validates a users input to ensure it is a valid string.
    Time: O(1).
    """

    if not isinstance(user_input, str):
        raise TypeError("Input must be a string.")

    return user_input.lower().replace(" ", "")


def compare_reversed_str(text: str) -> bool:
    """
    Compares a string to its reversed order to determine if it is a palindrome.
    Returns bool, Time: O(n), Space: O(n), where n is the number of characters in the string.
    """
    return text == text[::-1]


def format_result(result: bool, raw_input: str) -> str:
    """
    Returns a string result of the bool value.
    """
    if result:
        return f"'The string {raw_input}' is a palindrome!"
    else:
        return f"Sorry, '{raw_input}' is not a palindrome."


def main() -> None:
    print(intro_msg())
    raw_input = input(PROMPT_MSG)

    try:
        user_string = validate_input(raw_input)
        is_palindrome = compare_reversed_str(user_string)
        print(format_result(is_palindrome, raw_input))
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
