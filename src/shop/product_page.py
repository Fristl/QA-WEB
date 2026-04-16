"""Product card page."""
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.shop.base_page import ShopBasePage


class ProductPage(ShopBasePage):
    """Product card page."""

    PRICE = (By.CLASS_NAME, "price-new")
    CART_BUTTON = (By.ID, "button-cart")

    def __init__(
        self,
        browser: WebDriver,
        base_url: str,
        path: str,
        title: str,
        price: int,
    ):
        super().__init__(browser, base_url, path)
        self.title = title
        self.price = price

    @property
    def price_text(self) -> str:
        """The price element text."""
        return self.get_element(self.PRICE).text

    def is_loaded(self) -> bool:
        """Check the product card is shown."""
        self.wait_for_visible_element((By.XPATH, f"//h1[text()='{self.title}']"))
        self.wait_for_visible_element(self.CART_BUTTON)
        return bool(re.search(rf"{self.price}", self.price_text))
