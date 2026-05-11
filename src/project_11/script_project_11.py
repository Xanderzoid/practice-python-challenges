"""
Check Primality Functions
-------------------------
A CLI app that ask the user for a integer and determine whether the integer is prime or not.
"""


# Input: user integer
# Validate Input:
def validate_input() -> int:
    while True:
        raw = input("Enter a integer between (1-100): ")
        try:
            user_input = int(raw.replace(" ", ""))
            if not (0 < user_input <= 100):
                raise ValueError
        except ValueError:
            print(f"Invalid Input '{raw}'.")
            continue
        return user_input


# Process: Evaluate if user's integer is prime
# Evaluate prime:
def is_prime(num: int) -> bool:
    """
    Evaluate if a integer is a prime.
    Time: O(sqrt(n))
    """
    num_is_prime = True
    if num == 1:  # 1 edge case
        return False
    for i in range(2, int(num**0.5) + 1):  # Better than (2, n+1) -> O(n)
        if num % i == 0:
            num_is_prime = False
    return num_is_prime


# Find divisors:
def find_divisors(num: int) -> list:
    """
    Computes all positive divisors of an integer.
    Time: O(n)
    """
    divisor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list


# Ouptut: Display if the user's integer is prime or its divisors
# Into text:
def msg_logo() -> str:
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
    msg = "A CLI app that ask the user for a integer and determine whether the integer is prime or not."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


# Result text:
def prime_str(user_input: int) -> str:
    return f"Yes, {user_input} is a prime number!"


def divisors_str(user_input: int) -> str:
    divisor_list = find_divisors(user_input)
    divisor_string = ", ".join([str(x) for x in divisor_list])
    divisor_msg = f"No, {user_input} is not a prime number.\n{user_input} divisors are: {divisor_string}."
    return divisor_msg


# Run program:
def main() -> None:
    print(msg_logo())
    user_input = validate_input()
    result = is_prime(user_input)
    if result:
        print(prime_str(user_input))
    else:
        print(divisors_str(user_input))


if __name__ == "__main__":
    main()
