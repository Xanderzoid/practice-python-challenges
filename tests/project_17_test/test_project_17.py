import pytest
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from bs4 import BeautifulSoup
from project_17.script_project_17 import (
    url_scrapper,
    extract_articles_title,
    validate_input,
)


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("y", True),
        ("Yes", True),
        ("", True),
        ("q", False),
        ("Quit", False),
        ("arf6533", False),
    ],
)
def test_validate_input(input_str, expected):
    assert validate_input(input_str) == expected


def test_url_scrapper():
    soup = url_scrapper("https://httpbin.org/get")
    # Ensure soup isn't None (if url_scrapper returns None on error)
    assert soup is not None

    # Ensures timeout=10 works
    soup = url_scrapper("https://httpbin.org/delay/5")
    assert soup is not None


def test_url_scrapper_errors():
    with pytest.raises(HTTPError):
        url_scrapper("https://httpbin.org/status/404")
    with pytest.raises(Timeout):
        url_scrapper("https://httpbin.org/delay/15")


@pytest.mark.parametrize(
    "input_str, expected",
    [
        (
            """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nested Elements Sample</title>
</head>
<body>

    <a href="https://example01.com">
        <div>
            <p>Article Title 01</p>
        </div>
    </a>
    <a href="https://example02.com">
        <div>
            <p>Article Title 02</p>
        </div>
    </a>

</body>
</html>
""",
            ["Article Title 01", "Article Title 02"],
        )
    ],
)
def test_extract_articles_title(input_str, expected):
    soup = BeautifulSoup(input_str, "html.parser")
    assert extract_articles_title(soup) == expected
