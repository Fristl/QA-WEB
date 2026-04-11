"""Login admin page."""
from selenium.webdriver.common.by import By

from src.base import BasePage


class AdminLoginPage(BasePage):
    """Login admin page."""

    PATH = "administration"

    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    TITLE = (By.CLASS_NAME, "card-header")

    def is_loaded(self) -> bool:
        """
        Method to verify that the login page
        contains all required elements.
        """
        self.get_element(self.USERNAME)
        self.get_element(self.PASSWORD)
        self.get_element(self.SUBMIT)
        return self.title_text == "Please enter your login details."

    @property
    def title_text(self) -> str:
        """Method to verify that the user on the admin login page."""
        return self.get_element(self.TITLE).text

