""""
Write to a file 
--------------- 
A CLI app that write to file a list of qoutes.    
"""

# import
from pathlib import Path

# Global Constants
QUOTE_EINSTEIN = "'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.' -- Albert Einstein"
QUOTE_JANE = "'The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.' -- Jane Austen"
QUOTE_MONROE = "'Imperfection is beauty, madness is genius and it is better to be absolutely ridiculous than absolutely boring.' -- Marilyn Monroe"
QUOTES = [QUOTE_EINSTEIN, QUOTE_JANE, QUOTE_MONROE]

FILEPATH = "./data/quotes"

# Input:
#   sanitize
def sanitize_input(raw: str) -> str:
    """Removes leading and trailing whitespace and internal spaces from the input string and converts to lowercase."""
    return raw.strip().lower().replace(" ", "")

#   validate
def validate_input(cleaned: str) -> bool:
    """Checks if the user entered only letters."""
    if cleaned == "":
        return True
    else:
        return cleaned.isalpha()

#   User commmand
def quit_or_continue(cleaned: str) -> str:
    """Checks if the user wants to quit or continue."""
    if cleaned in ["q", "quit", "exit"]:
        return "q"
    elif cleaned in ["y", "yes", "start", "", "n", "no", "next", "exit"]:
        return "y"
    else:
        return "invalid"

# Process:
#   Check if file and path exist
def has_filepath(filepath: str) -> bool:
    """Checks if file and path exist."""
    path = Path(filepath)
    return path.exists()

#   Write to file
def write_to_file(quotes: list[str], path: str) -> bool:
    """Writes data to file."""
    data = ""
    for quote in quotes:
        data += f"{quote}\n"
    try:
        with open(path, "w") as file:
            file.write(data)
        return True
    except OSError:
        return False

#   Find a new file name if the file already exist
def find_new_filename(path: str) -> str:
    """Find a new file name if the file already exist."""
    count = 1
    while True:
        new_filename = f"{path}_{count}.txt"
        if not Path(new_filename).is_file():
            return new_filename
        count += 1

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
    msg = "A CLI app that write to file a list of qoutes."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}" + "\n"

#   Display status of writing data to file
def display_status(status: bool) -> str:
    """Displays status of writing data to file."""
    if status:
        return ("Data successfully written to file.")
    else:
        return ("Error writing data to file.")

#   Display quotes
def display_quotes(data: list[str] = QUOTES) -> str:
    """Displays quotes."""
    data_str = ""
    for quote in data:
        data_str += f"{quote}\n"
    return data_str

# Run program
def main() -> None:
    filepath = f"{FILEPATH}.txt"
    print(logo())
    print(display_quotes())
    while True:
        raw = input("Enter 'y' to start or 'q' to quit: ")
        user_input = sanitize_input(raw)
        if not validate_input(user_input):
            print(f"Invalid Input: {raw}. Enter letters only.")
            continue
        if quit_or_continue(user_input) == "q":
            print("\nEnd program...")
            break
        elif quit_or_continue(user_input) == "invalid":
            print(f"Invalid Input: {raw}. Enter 'y' or 'n' only.")
            continue
        if has_filepath(filepath):
            new_filename = find_new_filename(filepath)
            print(f"File already exist. New file name: {new_filename}")
            filepath = new_filename
        status = write_to_file(QUOTES, filepath)
        print(display_status(status))
        print("\nEnd program...")
        break


if __name__ == "__main__":
    main()
