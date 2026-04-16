"""Product page E2E tests."""
from selenium.webdriver.remote.webdriver import WebDriver

from src.shop import HomePage


def test_add_macbook_to_cart(browser: WebDriver, base_url: str) -> None:
    """Test add MacBook to cart and validate count and cart content."""
    home = HomePage(browser, base_url).open_page()
    cart_count = home.cart.count()
    home.add_product_to_cart("MacBook")
    cart_count += 1

    assert "MacBook" in home.success_alert_text(), \
        f"MacBook isn't in {home.success_alert_text()}"

    home.cart.wait_count_has_value(cart_count)
    assert home.cart.count() == cart_count

    home.cart.open()
    assert "MacBook" in home.cart.get_product_text()
