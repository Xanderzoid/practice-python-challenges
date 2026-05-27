"File reading and writing functions."
# Imports
from pathlib import Path

# Does the file exist
def find_file(filepath: str) -> bool:
    "Checks if file and path exist."
    path = Path(filepath)
    return path.exists()
    
# Read data from file
def read_from_file(filepath: str) -> list[str]:
    "Reads data from file."
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.readlines()
    except OSError:
        return []

# Clean the list of data of newline characters
def clean_data(data: list[str]) -> list[str]:
    "Cleans list of data of newline characters."
    return [line.strip() for line in data]
