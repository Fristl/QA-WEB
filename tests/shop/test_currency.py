"""Main page E2E tests."""
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.shop import HomePage


@pytest.mark.parametrize(
    ("currency_code", "expected_symbol"),
    [
        ("EUR", "€"),
        ("GBP", "£"),
        ("USD", "$"),
    ],
)
def test_currency_change_on_main(
    browser: WebDriver,
    base_url: str,
    currency_code: str,
    expected_symbol: str,
) -> None:
    """Switch currency test."""
    home = HomePage(browser, base_url).open_page()
    home.header.switch_currency(currency_code, expected_symbol)
    after = home.header.current_currency_text()

    assert expected_symbol in after, \
        f"There isn't {expected_symbol} in currency text after switching."


def test_default_currency(
    browser: WebDriver,
    base_url: str,
) -> None:
    """Default currency test."""
    home = HomePage(browser, base_url).open_page()
    assert home.header.current_currency_text() == "$ Currency", \
        f"Wrong default currency {home.header.current_currency_text()}"
