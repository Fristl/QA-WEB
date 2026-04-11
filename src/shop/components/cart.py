"""Cart dropdown."""
from selenium.webdriver.common.by import By

from src.base import BasePage


class CartDropdown:
    """Cart dropdown element of the page."""

    CART = (By.ID, "header-cart")
    BUTTON = (By.XPATH, "//*[@id='header-cart']/div/button")
    DROPDOWN = (By.CSS_SELECTOR, ".dropdown-menu.show")

    def __init__(self, page: BasePage):
        self.page = page

    def open(self) -> None:
        """Open cart dropdown."""
        self.page.click(self.BUTTON)
        self.page.get_element(self.DROPDOWN)

    def get_product_text(self) -> str:
        """Find product in the cart dropdown."""
        return self.page.get_element(self.DROPDOWN).text

    def count(self) -> int:
        """Count of items in cart."""
        return int(self.page.get_element(self.CART).text.split()[0])

    def wait_count_has_value(self, counter: int) -> None:
        """Wait updated counter."""
        self.page.wait_for_condition(
            condition=lambda _: self.count() == counter,
        )




