"""Base page of shop."""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


from src.base import BasePage
from src.shop.components import CartDropdown
from src.shop.components import Header


class ShopBasePage(BasePage):
    """Base class of shop's page."""

    SEARCH = (By.NAME, "search")
    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    SHOPPING_CART = (By.LINK_TEXT, "Shopping Cart")
    CHECKOUT = (By.LINK_TEXT, "Checkout")


    def __init__(self, browser: WebDriver, base_url: str, path: str = ""):
        super().__init__(browser, base_url, path)
        self.header = Header(self)
        self.cart = CartDropdown(self)
