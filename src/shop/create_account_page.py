"""Create user account page."""
import allure
from selenium.webdriver.common.by import By

from src.shop.base_page import ShopBasePage


class RegisterPage(ShopBasePage):
    """Create the user account page."""

    PATH = "en-gb?route=account/register"

    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    PRIVACY_CHECKBOX = (By.NAME, "agree")
    SUBMIT = (By.XPATH, "//*[@id='form-register']/div/button")
    SUCCESS_TITLE = (
        By.XPATH,
        "//h1[contains(text(), 'Your Account Has Been Created')]",
    )

    @allure.step("Check if registration page is loaded")
    def is_loaded(self) -> bool:
        """
        Method to verify that the registration page
        contains all required elements.
        """
        self.get_element(self.FIRSTNAME)
        self.get_element(self.LASTNAME)
        self.get_element(self.EMAIL)
        self.get_element(self.PASSWORD)
        self.get_element(self.SUBMIT)
        return True

    @allure.step("Input credentials for user and try to submit form.")
    def register(
        self,
        firstname: str,
        lastname: str,
        email: str,
        password: str,
    ) -> None:
        self.input_value(self.FIRSTNAME, firstname)
        self.input_value(self.LASTNAME, lastname)
        self.input_value(self.EMAIL, email)
        self.input_value(self.PASSWORD, password)
        self.click(self.PRIVACY_CHECKBOX)
        self.click(self.SUBMIT)

    @allure.step("New user was created")
    def is_success(self) -> bool:
        self.get_element(self.SUCCESS_TITLE)
        return True
