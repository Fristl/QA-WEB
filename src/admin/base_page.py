"""Base page of shop."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions

from src.base import BasePage


class AdminBasePage(BasePage):
    """Base class of shop's page."""

    LOGOUT = (By.ID, "nav-logout")
    PROFILE = (By.ID, "nav-profile")
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

    def __init__(
        self,
        browser: WebDriver,
        base_url: str,
        admin_credentials: dict[str, str],
        path: str = "",
    ):
        super().__init__(browser, base_url, path)
        self.admin_credentials = admin_credentials

    def login(self) -> None:
        """Login method."""
        self.input_value(self.USERNAME, self.admin_credentials["username"])
        self.input_value(self.PASSWORD, self.admin_credentials["password"])
        self.click(self.SUBMIT)

    def is_not_login(self) -> bool:
        self.wait.until(
            expected_conditions.invisibility_of_element_located(
                self.PROFILE,
            ),
        )
        self.wait.until(
            expected_conditions.invisibility_of_element_located(
                self.LOGOUT,
            ),
        )
        return True

    def open_page(self):  # noqa: ANN201
        """Open page."""
        super().open_page()
        if self.is_not_login():
            self.login()
        return self

