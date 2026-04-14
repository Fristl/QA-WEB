"""Product page E2E tests."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .conftest import wait_for_by
from .conftest import wait_for_condition


@pytest.mark.parametrize(
    ("currency_code", "expected_price"),
    [
        ("EUR", "95.72€"),
        ("GBP", "£74.73"),
    ],
)
def test_product_price(
    browser: WebDriver,
    base_url: str,
    currency_code: str,
    expected_price: str,
) -> None:
    """Verification of elements on the product page."""
    browser.get(
        f"{base_url}/en-gb/product/imac",
    )
    wait_for_by(
        browser,
        by=By.XPATH,
        value="//h1[text()='iMac']",
    )

    price_before = wait_for_by(
        browser,
        by=By.CLASS_NAME,
        value="price-new",
    ).text

    # Switch currency
    wait_for_by(
        browser,
        by=By.XPATH,
        value="//*[@id='form-currency']/div/a",
    ).click()
    wait_for_by(
        browser,
        by=By.XPATH,
        value=f"//a[@href='{currency_code}']",
    ).click()

    wait_for_condition(
        browser,
        condition=lambda browser: (
            browser.find_element(
                by=By.CLASS_NAME,
                value="price-new",
            ).text != price_before
        ),
    )

    price_after = wait_for_by(
        browser,
        by=By.CLASS_NAME,
        value="price-new",
    ).text

    assert price_after == expected_price, \
        f"Expected price {expected_price}, but got {price_after}"
