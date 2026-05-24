# Imports
import requests, pytest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
from project_19.script_project_19 import (
    sanitize_input,
    validate_selection,
    selected_hyperlink,
    webscrape_url,
    validate_input_is_int,
)


@pytest.mark.parametrize(
    "raw, expected",
    [
        (" 1 ", "1"),
        ("\t2\n", "2"),
        (" 3  ", "3"),
        ("abc", "abc"),
    ],
)
def test_sanitize_input(raw, expected):
    assert sanitize_input(raw) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("1", True),
        ("99", True),
        ("100", False),
        ("abc", False),
        ("sd1", False),
        ("", False),
    ],
)
def test_validate_input_is_int(user_input, expected):
    assert validate_input_is_int(user_input) == expected


@pytest.mark.parametrize(
    "user_input, hyperlinks, expected",
    [
        ("1", {"url1": "http://example01.com", "url2": "http://example02.com"}, "url1"),
        ("2", {"url1": "http://example01.com", "url2": "http://example02.com"}, "url2"),
        (
            "3",
            {"url1": "http://example01.com", "url2": "http://example02.com"},
            "invalid",
        ),
        (
            "abc",
            {"url1": "http://example01.com", "url2": "http://example02.com"},
            "invalid",
        ),
    ],
)
def test_validate_selection(user_input, hyperlinks, expected):
    assert validate_selection(user_input, hyperlinks) == expected


@pytest.mark.parametrize(
    "user_selection, hyperlinks, expected",
    [
        (
            "url1",
            {"url1": "http://example01.com", "url2": "http://example02.com"},
            "http://example01.com",
        ),
        (
            "url2",
            {"url1": "http://example01.com", "url2": "http://example02.com"},
            "http://example02.com",
        ),
    ],
)
def test_selected_hyperlink(user_selection, hyperlinks, expected):
    assert selected_hyperlink(user_selection, hyperlinks) == expected


@pytest.fixture
def sample_webpage():
    # HTML to mimic the true structure of quotes.toscrape.com
    return """
    <html>
        <body>
            <div class="quote">
                <span class="text">"Quote text 01"</span>
                <small class="author">Author 01</small>
            </div>
            <div class="quote">
                <span class="text">"Quote text 02"</span>
                <small class="author">Author 02</small>
            </div>
            <a href="/author/Author-01">Link 1</a>
            <a href="/author/Author-02">Link 2</a>
        </body>
    </html>
    """


@patch("requests.get")
def test_webscrape_url(mock_get, sample_webpage):
    # Simulate a successful requests response with a 200 status code
    mock_response = Mock()
    mock_response.text = sample_webpage
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Action:
    quit_toggle = True
    result = webscrape_url("https://quotes.toscrape.com", quit_toggle)

    # Assert: Check against the exact formatted string appended by webscrapper_url
    assert '"Quote text 01" - Author 01' in result["content"]
    assert '"Quote text 02" - Author 02' in result["content"]

    assert result["hyperlinks"] == {
        "url0": "Quit",
        "url1": "https://quotes.toscrape.com/author/Author-01",
        "url2": "https://quotes.toscrape.com/author/Author-02",
    }
