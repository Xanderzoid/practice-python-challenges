"""
Divisors
--------
A CLI utility that takes a number from a user then prints all divisors of that number.
"""


# logo and intro
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
    msg = "This CLI app that takes a number from a user then prints all divisors of that number."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


# Validate user input
def validate_input() -> int:
    while True:
        raw_input = input("Enter a number: ").replace(" ", "")
        try:
            num = int(raw_input)
            if num > 100 or num < 0:
                print(f"The number {num} is to large/small. Enter a valid number.")
                continue
            else:
                return num
        except ValueError:
            print(f"Invalid Input {raw_input}: Please enter a digit.")


# Compute a list of all divisors
def cal_divisors(num: int) -> list:
    num_list = [x for x in range(1, num + 1)]
    divisor_list = [x for x in num_list if num % x == 0]
    return divisor_list


# Result msg
def result_msg(num: int, divisor_list: list) -> str:
    msg = f"The number {num} has {len(divisor_list)} divisor/s they are {divisor_list}."
    return msg


# Run program
def run_app() -> None:
    print(intro_msg())
    user_num = validate_input()
    divisor_list = cal_divisors(user_num)
    print(result_msg(user_num, divisor_list))


if __name__ == "__main__":
    run_app()
