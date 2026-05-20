"""
Decode A Web Page
-----------------
A CLI app that prints out the article titles for the New York Time homepage.
"""
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from bs4 import BeautifulSoup


# Global Constants
URL = "https://www.nytimes.com"


# Input:
#   Validate input
def validate_input(raw_string: str) -> bool:
    """Parses if the user wants to webscrape."""
    user_input = raw_string.lower().replace(" ", "")
    return user_input in ["y", "yes", ""]


# Process:
#   Scrap url
def url_scrapper(url: str = URL) -> str | None:
    """Returns a BeautifulSoup object of the New York Time's homepage."""
    try:
        html_doc = requests.get(url, timeout=10)
        html_doc.raise_for_status()
        soup = BeautifulSoup(html_doc.text, "html.parser")
        return soup
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except ConnectionError:
        print("Error: Could not connect to the server.")
        raise
    except Timeout:
        print("Error: The request timed out.")
        raise
    except RequestException as err:
        print(f"An unexpected error occurred: {err}")
        raise


#   Extract data
def extract_articles_title(soup: BeautifulSoup) -> list[str]:
    """Returns a list of article titles from a HTML string."""
    seen = set()

    # Targeting only the (a > div > p) pattern
    articles = []
    for p_tag in soup.find_all("p"):
        parent = p_tag.parent

        # Check for (a > div > p)
        if parent.name == "div" and parent.parent and parent.parent.name == "a":
            text = p_tag.get_text().strip()
            # Remove dupe titles
            if text and text not in seen:
                articles.append(text)
                seen.add(text)
    return articles


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
    msg = "A CLI app that prints out the article titles for the New York Time homepage."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


#   Results
def display_results(articles: list[str]) -> str:
    """Returns the formated webscraped results."""
    msg = f"\n----Titles of articles----"
    for article in articles:
        msg += f"\n{article}"
    return msg


# Run program:
def main() -> None:
    print(logo())
    while True:
        raw_input = input("Webscrape The New York Times homepage[Y,n]: ")
        if not validate_input(raw_input):
            print("End program...")
            break

        try:
            soup = url_scrapper()
            if soup is None:
                break
            articles = extract_articles_title(soup)
            print(display_results(articles))
        except RequestException:
            print("Scraping failed. Exiting loop.")
            break
        break


if __name__ == "__main__":
    main()
