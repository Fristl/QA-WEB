"""Main page E2E tests."""
import re

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .conftest import wait_for_by
from .conftest import wait_for_condition


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
    browser.get(base_url)

    currency_before = wait_for_by(
        browser,
        by=By.XPATH,
        value="//*[@id='form-currency']/div/a",
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

    if  bool(re.search(rf"{expected_symbol}", currency_before)):
        _currency = wait_for_by(
            browser,
            by=By.XPATH,
            value="//*[@id='form-currency']/div/a",
        ).text
        assert currency_before == _currency, \
            f"When use the same currency - {_currency} something goes wrong"
    else:
        wait_for_condition(
            browser,
            condition=lambda browser: browser.find_element(
                By.XPATH,
                "//*[@id='form-currency']/div/a",
            ).text != currency_before,
        )

        currency_after = browser.find_element(
            By.XPATH,
            "//*[@id='form-currency']/div/a",
        ).text

        assert currency_before != currency_after, \
            f"Currency did not change after switching to {currency_code}"
        assert expected_symbol in currency_after, \
            (
                f"Expected symbol '{expected_symbol}' "
                f"not found in currency after switching to {currency_code}",
            )


def test_default_currency(
    browser: WebDriver,
    base_url: str,
) -> None:
    """Default currency test."""
    browser.get(base_url)
    default_currency = wait_for_by(
        browser,
        by=By.XPATH,
        value="//*[@id='form-currency']/div/a",
    )
    assert default_currency.text.strip() == "$ Currency", \
        f"Wrong default currency {default_currency.text}"
