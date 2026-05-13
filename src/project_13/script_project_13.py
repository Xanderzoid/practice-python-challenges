"""
Fibonacci
---------
This CLI app generates a Fibonacci sequence on integers of length given by the user.
"""

from collections.abc import Iterator


# Input:
# Validate input
def parse_and_validate(raw: str) -> int:
    cleaned = raw.lower().replace(" ", "")
    # Quit condition
    if cleaned in ["q", "quit", "exit", "0"]:
        return 0

    val = int(float(cleaned))
    if not (1 <= val <= 20):
        raise ValueError("Number out of range")
    return val


# Process:
# Generate Fibonacci list
def get_fibonacci_sequence(length: int) -> Iterator[int]:
    """Generates a fibonacci sequence of length 'length'."""
    a, b = 1, 1
    for _ in range(length):
        yield a
        a, b = b, a + b


# Output:
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
    msg = "A CLI app generates a Fibonacci sequence on integers of length given by the user."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


# Run program
def main() -> None:
    print(logo())
    while True:
        raw_val = input("Enter a number (1-20) or 'q' to quit: ")
        try:
            user_val = parse_and_validate(raw_val)
            if user_val == 0:
                print("End program...")
                break
            else:
                # Fibonacci sequence
                f_sequence = list(get_fibonacci_sequence(user_val))
                print(f"Fibonacci sequence length {user_val}: {f_sequence}")
        except (ValueError, TypeError):
            print(f"Invalid Input {raw_val}: Try again.")
            continue


if __name__ == "__main__":
    main()
