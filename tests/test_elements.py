"""Component tests for UI elements."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from .conftest import wait_for_by


@pytest.mark.parametrize(
    ("wait_by", "value_wait_by"),
    [
        (By.ID, "logo"),
        (By.NAME, "search"),
        (By.LINK_TEXT, "My Account"),
        (By.LINK_TEXT, "Shopping Cart"),
        (By.LINK_TEXT, "Checkout"),
    ],
)
def test_homepage_elements(
    browser: WebDriver,
    base_url: str,
    wait_by: ByType,
    value_wait_by: str,
) -> None:
    """Verification of elements on the main page."""
    browser.get(base_url)
    wait_for_by(browser, by=wait_by, value=value_wait_by)


def test_catalog_page(
    browser: WebDriver,
    base_url: str,
) -> None:
    """Verification of elements on the catalog page."""
    browser.get(f"{base_url}/en-gb/catalog/desktops")
    wait_for_by(browser, by=By.XPATH, value="//h2[text()='Desktops']")
    wait_for_by(browser, by=By.CLASS_NAME, value="product-thumb")
    wait_for_by(browser, by=By.ID, value="input-sort")
    sort_dropdown = wait_for_by(browser, by=By.ID, value="input-sort")
    select = Select(sort_dropdown)
    actual_options = [option.text for option in select.options]
    expected_options = [
        "Default",
        "Name (A - Z)",
        "Name (Z - A)",
        "Price (Low > High)",
        "Price (High > Low)",
        "Rating (Highest)",
        "Rating (Lowest)",
        "Model (A - Z)",
        "Model (Z - A)",
    ]
    assert actual_options == expected_options, \
        f"Expected {expected_options}, but got {actual_options}"


def test_product_page(
    browser: WebDriver,
    base_url: str,
) -> None:
    """Verification of elements on the product page."""
    expected_price = "$122.00"

    browser.get(
        f"{base_url}/en-gb/product/desktops/hp-lp3065",
    )
    wait_for_by(
        browser,
        by=By.XPATH,
        value="//h1[text()='HP LP3065']",
    )

    price_element = wait_for_by(browser, by=By.CLASS_NAME, value="price-new")
    price_text = price_element.text
    assert price_text == expected_price, \
        f"Expected price {expected_price}, but got {price_text}"

    wait_for_by(browser, by=By.CLASS_NAME, value="rating")
    wait_for_by(browser, by=By.ID, value="button-cart")


def test_admin_login(
    browser: WebDriver,
    base_url: str,
) -> None:
    """Verification of login elements on the admin page."""
    browser.get(f"{base_url}/administration/")
    expected_title = "Please enter your login details."

    wait_for_by(browser, by=By.ID, value="input-username")
    wait_for_by(browser, by=By.ID, value="input-password")
    wait_for_by(browser, by=By.XPATH, value="//button[@type='submit']")

    title_element = wait_for_by(browser, by=By.CLASS_NAME, value="card-header")
    title = title_element.text
    assert title.strip() == expected_title, \
        f"Expected title {expected_title}, but got {title}"
    wait_for_by(browser, by=By.TAG_NAME, value="footer")


def test_register_page(
    browser: WebDriver,
    base_url: str,
) -> None:
    """Verification of registration elements on the user page."""
    browser.get(f"{base_url}/en-gb?route=account/register")
    wait_for_by(browser, by=By.ID, value="input-firstname")
    wait_for_by(browser, by=By.ID, value="input-lastname")
    wait_for_by(browser, by=By.ID, value="input-email")
    wait_for_by(browser, by=By.ID, value="input-password")
    wait_for_by(browser, by=By.XPATH, value="//button[@type='submit']")
