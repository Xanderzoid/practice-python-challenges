"""
List Less Than Ten
------------------
A CLI utility to that displays all numbers within a list less the user's input number.
"""
REFERENCE_LIST = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def intro_msg() -> str:
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
    msg = "This CLI app displays all numbers within a list less than your number."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


def display_list(num_list: list) -> str:
    msg = f"Number List: {num_list}"
    return msg


def display_result(user_num: float, num_list: list) -> str:
    result_list = compute_list(user_num, num_list)
    if result_list:
        msg = f"List of numbers less than {int(user_num)}: {result_list}"
    else:
        msg = f"There are no numbers less than {int(user_num)}."
    return msg


def validate_input() -> float:
    while True:
        raw_input = input("Enter your number: ").replace(" ", "")
        try:
            num = float(raw_input)
            return num
        except ValueError:
            print(f"Invalid Input {raw_input}: Please enter a digit.")


def compute_list(user_num: float, num_list: list) -> list:
    result_list = [x for x in num_list if x < user_num]
    return result_list


def run_app() -> None:
    # Print intro
    print(intro_msg())
    print(display_list(REFERENCE_LIST))

    # Logic
    user_num = validate_input()

    # Output
    print(display_result(user_num, REFERENCE_LIST))


if __name__ == "__main__":
    run_app()
