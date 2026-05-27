"""
Read From File 
-------------- 
A CLI app that reads data from a file and counts the number of repeated words.
"""

# Imports:
import project_22.file_io as file_io

# Global Constants:
FILEPATH = "./data/data.txt"

# Input:
#   sanitize
def sanitize_input(input: str) -> str:
    "Removes leading and trailing whitespace and internal spaces from the input string."
    return input.lower().strip().replace(" ", "")

#   validate
def validate_input(input: str) -> str:
    "Validates user input."
    if input in ["y", "yes", "start", ""]:
        return 'y'
    elif input in ["n", "no", "q", "quit"]:
        return 'q'
    else:
        return "invalid"
# Process:
#   Count the number of repeated words.
def count_repeated_words(data: list[str]) -> dict[str, int]:
    "Counts the number of repeated words."
    reslut = {}
    for word in data:
        if word in reslut:
            reslut[word] += 1
        else:
            reslut[word] = 1
    return reslut
# Output:
#   Display data from file
def display_data(data: dict[str, int]) -> str:
    "Returns data from file."
    result = []
    for word, count in data.items():
        result.append(f"{word}: {count}")
    return "\n".join(result)
    
#   Intro
def logo() -> str:
    """Returns BLX Data.Mine logo."""
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
    msg = "A CLI app that reads data from a file and counts the number of repeated words."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}" + "\n"

# Run program:
def main() -> None:
    print(logo())
    while True:
        raw = input("Enter 'y' to start or 'q' to quit: ")
        user_input = sanitize_input(raw)
        if validate_input(user_input) == "q":
            print("\nEnd program...")
            break
        elif validate_input(user_input) == "invalid":
            print(f"Invalid Input: {raw}. Enter 'y' or 'n' only.")
            continue
        if file_io.find_file(FILEPATH):
            data = file_io.read_from_file(FILEPATH)
            cleaned_data = file_io.clean_data(data)
            result = count_repeated_words(cleaned_data)
            print(display_data(result))
            break
        else:
            print(f"File not found: {FILEPATH}")
            break

if __name__ == "__main__":
    main()
