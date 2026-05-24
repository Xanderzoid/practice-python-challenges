"""
Decode A Web Page Two
---------------------
A CLI app that reads a webpage of its main content and navigates the author's description.
Given the original project, use a site that has full content that is now longer forward facing.
I have substituted the original site with a new one that has similar content and structure.
The new site is https://quotes.toscrape.com/.
"""

# Imports
import requests
from bs4 import BeautifulSoup
from typing import cast

# Global Constants
URL = "https://quotes.toscrape.com"


# Input: Select a hyperlink
# Validate that the user selected a numerical index referencing a hyperlink on the page.
def sanitize_input(raw: str) -> str:
    """Removes leading and trailing whitespace and internal spaces from the input string."""
    return raw.strip().replace(" ", "")


def validate_input_is_int(user_input: str) -> bool:
    """Checks if the user input is an integer between 0 and 99."""
    try:
        user_int = int(user_input)
        if 0 <= user_int <= 99:
            return True
        else:
            return False
    except ValueError:
        return False


def validate_selection(user_input: str, hyperlinks: dict[str, str]) -> str:
    """Validates the user's selection and returns the corresponding key to hyperlink."""
    key_set = set(hyperlinks.keys())
    user_key = "url" + user_input
    if user_key not in key_set:
        return "invalid"
    return user_key


def selected_hyperlink(user_selection: str, hyperlinks: dict[str, str]) -> str:
    """Returns the hyperlink corresponding to the user's selection."""
    return hyperlinks[user_selection]


# Processing: Navigate to the hyperlink and read the main content of the page.
# Get the main content of the page and the hyperlinks on the page.
def url_scrapper(url: str) -> BeautifulSoup:
    """Returns a BeautifulSoup object of the webpage."""
    try:
        html_doc = requests.get(url, timeout=10)
        html_doc.raise_for_status()
        soup = BeautifulSoup(html_doc.text, "html.parser")
        return soup
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return BeautifulSoup(
            "<html><body>Error fetching URL</body></html>", "html.parser"
        )


def webscrape_url(url: str, quit_toggle: bool) -> dict[str, list[str] | dict[str, str]]:
    """
    Scrapes the URL and returns a dictionary with the content and hyperlinks.
    """
    soup = url_scrapper(url)
    text_author_list = []
    author_descript_list = []
    author_set = set()
    hyperlinks = {}

    # Back button text or quit button text
    if quit_toggle:
        hyperlinks[f"url{0}"] = "Quit"
    else:
        hyperlinks[f"url{0}"] = "Go Back"

    # Target div with class "author-description"
    author_div = soup.find("div", class_="author-description")

    if not author_div:
        # Target div with class "quote"
        for quote_div in soup.find_all("div", class_="quote"):
            # Extract the quote text and author
            span_tag = quote_div.find("span", class_="text")
            author_tag = quote_div.find("small", class_="author")
            if span_tag and author_tag:
                quote_text = span_tag.get_text()
                quote_author = author_tag.get_text()
                text_author_list.append(f"{quote_text} - {quote_author}")
        # Extract hyperlinks
        for idx, a_tag in enumerate(soup.find_all("a"), start=1):
            href = a_tag.get("href")
            if href and str(href).startswith("/author"):
                author_name = f"{URL}{href}"  # Remove dupe author names
                if author_name not in author_set:
                    hyperlinks[f"url{idx}"] = f"{URL}{href}"
                    author_set.add(author_name)
        return {"content": text_author_list, "hyperlinks": hyperlinks}
    else:
        for descript_div in soup.find_all("div", class_="author-description"):
            # Extract the description of the author
            descript_text = descript_div.get_text()
            author_descript_list.append(descript_text)
        return {"content": author_descript_list, "hyperlinks": hyperlinks}


# Output: Display homepage content and hyperlinks to the user after each selection.
# Intro
def logo() -> None:
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
    msg = "A CLI app that reads a webpage of its main content and navigates the author's description."
    spacer = "-" * len(msg)
    print(f"{ascii_art}\n{spacer}\n{msg}\n{spacer}" + "\n")


def display_text_author(webpage_content: list[str]) -> None:
    """Displays the main content of the webpage."""
    for item in webpage_content:
        print(item + "\n")


def display_links(hyperlinks: dict[str, str]) -> None:
    """Displays the hyperlinks on the webpage."""
    for key, value in hyperlinks.items():
        number = key.replace("url", "")
        if len(number) == 1:
            number = " " + number
        author = value.replace("https://quotes.toscrape.com/author/", "")
        print(f"{number}: {author}")


def display_content(url: str, quit_toggle) -> dict[str, str]:
    """Displays the content and hyperlinks of the webpage."""
    logo()
    website = webscrape_url(url, quit_toggle)
    content = cast(list[str], website["content"])
    hyperlinks = cast(dict[str, str], website["hyperlinks"])
    display_text_author(content)
    display_links(hyperlinks)
    return hyperlinks


# Run program
def main() -> None:
    url = URL
    quit_toggle = True

    while True:
        # Display intro
        hyperlinks = display_content(url, quit_toggle)

        # Get user input
        raw = input("\nEnter the next page number: ")
        user_input = sanitize_input(raw)

        if not validate_input_is_int(user_input):
            print(f"Invalid Input: {raw}")
            continue

        if validate_selection(user_input, hyperlinks) == "invalid":
            print(f"Invalid Selection: {raw}")
            continue

        # End program
        if user_input == "0" and quit_toggle:
            print("End program...")
            break

        # Update url and quit_toggle
        if user_input != "0":
            quit_toggle = False
            url = hyperlinks[f"url{user_input}"]
        if user_input == "0" and not quit_toggle:
            quit_toggle = True
            url = URL

        continue


if __name__ == "__main__":
    main()
