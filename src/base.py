"""Module with base things."""
from typing import Any
from typing import Callable
from urllib.parse import urljoin

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base page."""

    PATH = ""
    TIMEOUT = 10

    def __init__(self, browser: WebDriver, base_url: str, path: str = ""):
        self.browser = browser
        self._base_url = base_url
        self._path = path or self.PATH
        self.url = urljoin(self._base_url, self._path)
        self.wait = WebDriverWait(self.browser, self.TIMEOUT)

    @staticmethod
    def _text_xpath(text : str) -> str:
        return f"//*[text()='{text}']"

    def open_page(self):  # noqa: ANN201
        """Open page."""
        self.browser.get(self.url)
        return self

    def get_element(self, locator: tuple[str, str]) -> WebElement:
        """Find element."""
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator),
        )

    def get_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        """Find elements."""
        return self.wait.until(
            expected_conditions.visibility_of_all_elements_located(locator),
        )

    def click(self, locator: tuple[str, str]) -> None:
        """Click on the element with the user-like delay."""
        chains = ActionChains(self.browser)
        chains.move_to_element(
            self.get_element(locator),
        ).pause(
            0.5,
        ).click().perform()

    def input_value(self, locator: tuple[str, str], text: str) -> None:
        """Enter text to the input by single key."""
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for symbol in text:
            self.get_element(locator).send_keys(symbol)

    def wait_for_url_contains(self, part_of_url: str) -> None:
        """Waiter for URL."""
        self.wait.until(expected_conditions.url_contains(part_of_url))

    def execute_js(self, script: str, *args: Any) -> Any:
        """Execute JS script."""
        return self.browser.execute_script(script, *args)

    def click_checkbox(self, checkbox: WebElement, idx: int | str = 0) -> None:
        self.execute_js(f"arguments[{idx}].click()", checkbox)

    def wait_for_element(self, by: ByType, value: str) -> WebElement:
        """Explicit waiter."""
        return self.wait.until(
            expected_conditions.visibility_of_element_located((by, value)),
        )

    def wait_for_by(
        self,
        *,
        by: ByType | str,
        value: str,
    ) -> WebElement:
        return self.wait.until(
            expected_conditions.visibility_of_element_located((by, value)),
        )

    def wait_for_condition(
        self,
        *,
        condition: Callable,
    ) -> WebDriverWait:
        return self.wait.until(condition)

    def wait_for_contains_url(self, *, url_contains: str) -> bool:
        return self.wait.until(
            expected_conditions.url_contains(url_contains),
        )
