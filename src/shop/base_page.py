"""Base page of shop."""
from selenium.webdriver.remote.webdriver import WebDriver

from src.base import BasePage
from src.shop.components import CartDropdown
from src.shop.components import Header


class ShopBasePage(BasePage):
    """Base class of shop's page."""

    def __init__(self, browser: WebDriver, base_url: str, path: str = ""):
        super().__init__(browser, base_url, path)
        self.header = Header(self)
        self.cart = CartDropdown(self)
