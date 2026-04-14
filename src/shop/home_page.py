"""Home page."""
from selenium.webdriver.common.by import By

from src.shop.base_page import ShopBasePage


class HomePage(ShopBasePage):
    """Home page."""

    PRODUCT_CARD = (By.CLASS_NAME, "product-thumb")
    ADD_PRODUCT_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "button[title='Add to Cart']",
    )

    def add_product_to_cart(self, product_name: str) -> None:
        """Add product to cart."""
        # ensure products are visible
        self.get_element(self.PRODUCT_CARD)
        self.get_element(
            (
                By.XPATH,
                f"//a[text()='{product_name}']/ancestor::div[contains(@class, 'product-thumb')]",  # noqa: E501
            ),
        )
        add_to_cart_button = self.get_element(self.ADD_PRODUCT_TO_CART_BUTTON)
        self.wait_for_condition(
            condition=lambda _: add_to_cart_button.is_enabled() and
                                add_to_cart_button.is_displayed(),
        )
        # click via js, cause the regular selenium click doesn't work
        self.execute_js("arguments[0].click();", add_to_cart_button)

    def success_alert_text(self) -> str:
        """Alert."""
        return self.get_element((By.CSS_SELECTOR, ".alert-success")).text
