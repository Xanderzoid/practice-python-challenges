"""
Rock Paper Scissors
-------------------
This CLI plays the game rock, paper, scissors with the user.
"""
import random


# Input: Select rock, paper, or scissors
def get_hand(user_input: str) -> str:
    """
    Determines if input is a hand or quit message or invalid.
    Time: O(n) the use of .lower() and .replace().
    Space: O(n).
    """
    clean_input = user_input.lower().replace(" ", "")
    if clean_input in ["r", "p", "s"]:
        return clean_input
    if clean_input == "q":
        return "quit"
    raise ValueError(f"Invalid Input {user_input}: Enter 'r', 'p', 's', or 'q'")


def validate_input() -> None:
    """
    Process valid inputs and runs game logic.
    """
    while True:
        msg = "Enter 'r'(Rock) or 'p'(Paper) or 's'(Scissors): "
        raw = input(msg)
        try:
            user_input = get_hand(raw)
            if user_input == "quit":
                print("End program...")
                break
            else:
                computer_input = generate_hand()
                user_hand = hand_dict(user_input)
                computer_hand = hand_dict(computer_input)
                game_winner = game_logic(user_hand, computer_hand)
                print(display_result(game_winner, user_hand, computer_hand))
                continue
        except ValueError as e:
            print(e)


def hand_dict(text: str) -> dict:
    """Converts the string representation of the player/computer's hand to a dict."""
    result_dict = {"r": False, "p": False, "s": False}
    if text == "r":
        result_dict["r"] = True
    elif text == "p":
        result_dict["p"] = True
    else:
        result_dict["s"] = True
    return result_dict


# Process: Compute the winner and keep score
def generate_hand() -> str:
    """Returns str representation of a randomly selected hand."""
    hand = ["r", "p", "s"]
    return hand[random.randint(0, 2)]


def game_logic(player: dict, computer: dict) -> dict:
    """
    Compares player and computer's hand to evelauated who won.
    Time: O(1), fixed number of conditional statements.
    """
    # Tie
    if (
        (player["r"] and computer["r"])
        or (player["p"] and computer["p"])
        or (player["s"] and computer["s"])
    ):
        return {"player": True, "computer": True}
    # Rock wins
    elif (player["r"] and not computer["p"]) and (player["r"] and computer["s"]):
        return {"player": True, "computer": False}
    elif (computer["r"] and not player["p"]) and (computer["r"] and player["s"]):
        return {"player": False, "computer": True}
    # Paper wins
    elif (player["p"] and computer["r"]) and (player["p"] and not computer["s"]):
        return {"player": True, "computer": False}
    elif (computer["p"] and player["r"]) and (computer["p"] and not player["s"]):
        return {"player": False, "computer": True}
    # Scissors wins
    elif (player["s"] and not computer["r"]) and (player["s"] and computer["p"]):
        return {"player": True, "computer": False}
    elif (computer["s"] and not player["r"]) and (computer["s"] and player["p"]):
        return {"player": False, "computer": True}
    else:
        return {"player": False, "computer": False}


# Output: Display the computers hand, players hand, who is the winner.
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
    msg = "This CLI plays the game rock, paper, scissors with the user."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


def key_to_word(key: str) -> str:
    """Converts r, p,and s to Rock, Paper, and Scissors"""
    if key == "r":
        return "Rock"
    elif key == "p":
        return "Paper"
    else:
        return "Scissors"


def display_result(game: dict, player: dict, computer: dict) -> str:
    """
    Formats result text.
    Time: O(1), fixed dict length loop.
    """
    player_hand = ""
    computer_hand = ""
    for key, value in player.items():
        if value:
            player_hand = key_to_word(key)
    for key, value in computer.items():
        if value:
            computer_hand = key_to_word(key)

    if game["player"] and game["computer"]:
        win_msg = f"You both picked {player_hand}. Its a draw!"
    elif game["player"]:
        win_msg = f"The computer choose {computer_hand}. {player_hand} beats {computer_hand}. You won!"
    else:
        win_msg = f"Sorry, the computer choose {computer_hand}. {computer_hand} beats {player_hand}. The computer won :("
    retry_msg = "\nType 'q' to quit or enter anthor hand."
    return win_msg + retry_msg


def main() -> None:
    print(msg_logo())
    validate_input()


if __name__ == "__main__":
    main()
