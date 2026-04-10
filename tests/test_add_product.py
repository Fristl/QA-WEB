"""Product page E2E tests."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .conftest import wait_for_by
from .conftest import wait_for_condition


def test_add_macbook_to_cart(
    browser: WebDriver,
    base_url: str,
) -> None:
    """Test add MacBook to cart and validate count and cart content."""
    cart_counter = 0
    browser.get(base_url)

    wait_for_by(browser, by=By.CLASS_NAME, value="product-thumb")

    macbook = browser.find_element(
        By.XPATH,
        "//a[text()='MacBook']/ancestor::div[contains(@class, 'product-thumb')]",  # noqa: E501
    )
    add_to_cart_button = macbook.find_element(
        By.CSS_SELECTOR,
        "button[title='Add to Cart']",
    )

    wait_for_condition(
        browser,
        condition=lambda _: (
            add_to_cart_button.is_enabled() and
            add_to_cart_button.is_displayed()
        ),
    )
    browser.execute_script("arguments[0].click();", add_to_cart_button)
    cart_counter += 1

    success_alert = wait_for_by(
        browser,
        by=By.CSS_SELECTOR,
        value=".alert-success",
    )
    assert success_alert.is_displayed(), \
        f"Macbook {macbook} wasn't add to cart!"
    assert "MacBook" in success_alert.text, \
        f"Success alert doesn't have {macbook} in text"

    wait_for_condition(
        browser,
        condition=lambda browser: int(
            browser.find_element(By.ID, "header-cart").text.split()[0],
        ) == cart_counter,
    )

    cart_text_after = browser.find_element(By.ID, "header-cart").text
    count_after = int(cart_text_after.split()[0])
    assert count_after == cart_counter, \
        f"Cart count did not increase correctly, got {count_after}"

    cart_button = wait_for_by(
        browser,
        by=By.XPATH,
        value="//*[@id='header-cart']/div/button",
    )
    browser.execute_script("arguments[0].click();", cart_button)

    cart_dropdown = wait_for_by(
        browser,
        by=By.CSS_SELECTOR,
        value=".dropdown-menu.show",
    )
    assert "MacBook" in cart_dropdown.text
