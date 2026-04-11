"""Header of the OpenCart."""
import re

from selenium.webdriver.common.by import By

from src.base import BasePage


class Header:
    """Header of the page."""

    CURRENCY_TOGGLE = (By.XPATH, "//*[@id='form-currency']/div/a")

    def __init__(self, page: BasePage):
        self.page = page

    def current_currency_text(self) -> str:
        """Return currency."""
        return self.page.get_element(self.CURRENCY_TOGGLE).text

    def switch_currency(
        self,
        currency_code: str,
        expected_symbol: str,
    ) -> None:
        """Switch currency."""
        before = self.current_currency_text()
        self.page.click(self.CURRENCY_TOGGLE)
        self.page.click((By.XPATH, f"//a[@href='{currency_code}']"))

        if bool(re.search(rf"{expected_symbol}", before)):
            self.page.wait_for_condition(
                condition=lambda _: self.current_currency_text() == before,
            )
        else:
            self.page.wait_for_condition(
                condition=lambda _: self.current_currency_text() != before,
            )
