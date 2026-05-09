"""
Guessing Game One
-----------------
A CLI app that generates a random number between (1-9)
the user must guess the number and the program will
respond with too low, too high, or exactly right.
"""

import random

# Global Constants
GAME_RULES = "Enter a number between (1-9) to guess what the computer is thinking."


# Input: User guess
def game_logic() -> None:
    """Runs game logic in a loop until the user quits."""
    player_score = 0
    num_games = 0
    prompt_msg = "Enter you guess: "
    computer_input = random_int()  # Initial number
    print(msg_logo())
    print(GAME_RULES)
    print(scoreboard(num_games, player_score))
    while True:
        raw = input(prompt_msg)
        user_input = validate_input(raw)
        if user_input == None:
            continue
        elif user_input == 0:
            print("End program...")
            break
        else:
            compare_result = compare_num(user_input, computer_input)
            num_games, player_score, computer_input = update_score(
                num_games, player_score, compare_result, computer_input
            )
            print(display_results(user_input, compare_result))
            print(scoreboard(num_games, player_score))
            prompt_msg = "Continue or type 'exit' to quit program. Enter guess: "
            continue


def validate_input(raw: str) -> int | None:
    """Validate and convert user string into an int."""
    cleaned = raw.replace(" ", "")

    if cleaned in ["quit", "exit"]:
        return 0
    try:
        user_int = int(float(cleaned))
    except ValueError:
        print("Invalid Input. Enter a number (1-9) or type 'exit' to quit program.")
        return None

    if not 1.0 <= user_int <= 9.0:
        print("Invalid Input. Enter a number (1-9) or type 'exit' to quit program.")
        return None

    return user_int


# Process: Computer choise and compute distance for guess to computer choise
def random_int() -> int:
    """Generates a random int (1-9)"""
    return random.randint(1, 9)


def update_score(
    games: int, old_score: int, result: str, computer: int
) -> tuple[int, int, int]:
    """
    Updates score, number of game, and computer munber based on comparison result.
    Time: O(1), Space: O(1)
    """
    if result == "exactly right":
        # Generates a new computer number after winning
        return games + 1, old_score + 1, random_int()
    else:
        return games + 1, old_score, computer


# Output: Display game rules, comparision result, and game stats


def compare_num(player: int, computer: int) -> str:
    """
    Returns a string describing the closeness of the user's guess.
    Time: O(1), Space: O(1)
    """
    if player == computer:
        return "exactly right"
    elif player < computer:
        return "too low"
    else:
        return "too high"


def display_results(player: int, result) -> str:
    """Displays how close the user guess is from the computer's number."""
    if result == "exactly right":
        return f"Your number is {result}. You guesed the computer's number!"
    else:
        return f"Your number ({player}) is {result}, Try again."


def scoreboard(games: int, score: int) -> str:
    """Display games played and scoreboard."""
    return f"Number of games played: {games} Player's score: {score}"


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
    msg = "This CLI app that generates a random number between (1-9) the user must guess the number."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


if __name__ == "__main__":
    game_logic()
