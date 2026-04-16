"""Product page E2E tests."""
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.shop import ProductPage


@pytest.mark.parametrize(
    ("currency_code", "expected_symbol", "expected_price"),
    [
        ("EUR", "€", "95.72€"),
        ("GBP", "£", "£74.73"),
    ],
)
def test_product_price(
    browser: WebDriver,
    base_url: str,
    currency_code: str,
    expected_symbol: str,
    expected_price: str,
) -> None:
    """Verification of elements on the product page."""
    product = ProductPage(
        browser,
        base_url,
        "en-gb/product/imac",
        "iMac",
        122,
    ).open_page()
    assert product.is_loaded(), f"Page {product} is not loaded"

    # Switch currency
    product.header.switch_currency(currency_code, expected_symbol)
    assert product.price_text == expected_price, \
        f"Expected price {expected_price}, but got {product.price_text}"
