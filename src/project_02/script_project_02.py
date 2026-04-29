"""
Odd or Even
-----------
A CLI utility to determine if a users input number is odd or even.
"""


def result_msg(is_even: bool, num: float) -> str:
    if is_even:
        return f"The number {num} is even.\n"
    else:
        return f"The number {num} is odd.\n"


def validate_input() -> float:
    ascii_art = """                 
                 ###                                       
                ##  #                                      
               ## ####                                     
              ##  #   #             =======================
             ## #### ###            B L X   D A T A M I N E
            ##  #    #  #           =======================
           ## ####  ######               [Est. 2026]       
          ##  #   ###     #                                
         ## #### ##  ##  ###                                """
    msg = "This CLI app checks if a user's number is odd or even."
    spacer = "-" * len(msg)
    print(f"{ascii_art}\n{spacer}\n{msg}\n{spacer}")
    while True:
        raw_input = input("Enter your number: ").replace(" ", "")
        try:
            num = float(raw_input)
            return num

        except ValueError:
            print(f"Invalid input '{raw_input}': Enter a digit.")


def identify_even(num: float) -> bool:
    return num % 2 == 0


def run_app() -> None:
    num = validate_input()
    is_even = identify_even(num)
    result_str = result_msg(is_even, num)
    print(result_str)


if __name__ == "__main__":
    run_app()
