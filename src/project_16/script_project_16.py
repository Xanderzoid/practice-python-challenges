"""
Password Generator
A CLI app that generates a ASCII password.
"""
import random, math

# Global Constants
STRONG_UNI = 87
WEAK_UNI = 26
STRONG_CHARSET = [i for i in range(33, 127) if i not in [34, 39, 96, 44, 46, 124]]


# Input:
#   Sanitize input
def sanitize_type(raw: str) -> bool:
    """Determine if the password should be strong or not."""
    data = raw.lower().replace(" ", "")
    return data in ["yes", "y", "strong"]


def sanitize_input(raw: str) -> int:
    """Returns a clean integer for user input."""
    data = raw.replace(" ", "")
    try:
        data_int = round(float(data))
        if 8 <= data_int <= 25:
            return data_int
        return 0
    except ValueError:
        return 0


#   Validate user parameters
def validate_input(data: dict[str, int | bool]) -> bool:
    """Validates that the parameters are weak or strong and length within (8-25) characters."""
    if data["weak"] == True:
        return True
    elif data["strong"] == True and 8 <= data["length"] <= 25:
        return True
    else:
        return False


# Process:
#   Generate strong password
def strong_pass(length: int) -> dict[str, list[int] | str]:
    """
    Generates a strong ascii password length (8-25).
    Returns password and ascii representation.
    {"ascii": ascii_int, "password": ascii_str}
    """
    ascii_int = random.choices(STRONG_CHARSET, k=length)
    ascii_str = "".join([chr(x) for x in ascii_int])
    return {"ascii": ascii_int, "password": ascii_str}


#   Generate weak password
def weak_pass() -> dict[str, list[int] | str]:
    """
    Generates a weak ascii password of 8 characters.
    Returns password and ascii representation.
    {"ascii": ascii_int, "password": ascii_str}
    """
    words = [
        "blue",
        "fast",
        "glow",
        "high",
        "jump",
        "kind",
        "loud",
        "mind",
        "near",
        "open",
    ]
    ascii_str = "".join([words[random.randint(0, 9)] for _ in range(2)])
    ascii_int = [ord(x) for x in ascii_str]
    return {"ascii": ascii_int, "password": ascii_str}


#   Entropy Analysis
def analysis_entropy(data: dict[str, int]) -> float:
    """Calculates the entropy of a ascii password"""
    return round(data["L"] * math.log2(data["R"]), 2)


def cal_entropy(
    data: dict[str, list[int] | str], strength: bool
) -> dict[str, float | int]:
    """
    Returns the entropy of a ascii password and the number of unique characters.
    {"E": E, "unique_char": unique_char}
    """
    L = len(data["password"])
    R = STRONG_UNI if strength else WEAK_UNI
    E = analysis_entropy({"R": R, "L": L})
    unique_char = len(set(data["ascii"]))
    return {"E": E, "unique_char": unique_char}


# Output:
#   Intro
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
    msg = "A CLI app that generates a ASCII password."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


#   Results
def display_results(
    password: str, entropy: float, strength: bool, unique_char: int
) -> str:
    """Returns the password and stats message."""
    pass_type = "strong" if strength else "weak"
    msg = f"\nYour {pass_type} password is: {password}\nEntropy: {entropy} bits.\nEntropy {entropy} passwords are "
    if entropy <= 35:
        e_msg = "vulnerable to simple desktop brute-force attacks that will solve in minutes."
    elif 36 <= entropy <= 59:
        e_msg = "reasonable for low-stakes accounts; risky for sensitive data."
    elif 60 <= entropy <= 127:
        e_msg = "very difficult to crack; the target for most personal accounts."
    else:
        e_msg = "extremely strong; theoretically uncrackable by current technology."

    if unique_char < len(password) * 0.80:
        u_msg = f"\nYour password has low uniqueness, it's likely weaker than a {entropy} bit password."
    else:
        u_msg = "\nYour password has high uniqueness."
    return msg + e_msg + u_msg


# Run program
def main() -> None:
    run_program = True
    print(logo())
    while True:
        raw_type = input("Do you want a strong password? [y/N/q]: ")
        if raw_type.lower().replace(" ", "") in ["q", "quit"]:
            print("End program...")
            run_program = False
            break
        elif not sanitize_type(raw_type):
            pass_dict = weak_pass()
            is_strong = False
        else:
            while True:
                raw_length = input("Enter password length (8-25): ")
                length = sanitize_input(raw_length)
                if length == 0:
                    print(f"Invalid Input: {raw_length}")
                    continue
                pass_dict = strong_pass(length)
                is_strong = True
                break
        if not run_program:
            break
        entropy_dict = cal_entropy(pass_dict, is_strong)
        result_str = display_results(
            pass_dict["password"],
            entropy_dict["E"],
            is_strong,
            entropy_dict["unique_char"],
        )
        print(result_str)
        break


if __name__ == "__main__":
    main()
