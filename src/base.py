"""Module with base things."""
import logging
from pathlib import Path
from typing import Any
from typing import Callable
from urllib.parse import urljoin

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base page."""

    PATH = ""
    TIMEOUT = 30

    def __init__(self, browser: WebDriver, base_url: str, path: str = ""):
        self.browser = browser
        self._base_url = base_url
        self._path = path or self.PATH
        self.url = urljoin(self._base_url, self._path)
        self.wait = WebDriverWait(self.browser, self.TIMEOUT)
        self.logger = self.__config_logger(to_file=True)

    def __config_logger(self, *, to_file: bool = False) -> logging.Logger:
        logger = logging.getLogger(type(self).__name__)
        Path("logs").mkdir(exist_ok=True)
        if to_file:
            logger.addHandler(
                logging.FileHandler(f"logs/{self.browser.test_name}.log"))  # type: ignore[attr-defined]
        logger.setLevel(level=self.browser.log_level)  # type: ignore[attr-defined]
        return logger

    @staticmethod
    def _text_xpath(text : str) -> str:
        return f"//*[text()='{text}']"

    @allure.step("Open page")
    def open_page(self):  # noqa: ANN201
        """Open page."""
        self.logger.info("Open page %s", self.url)
        self.browser.get(self.url)
        return self

    @allure.step("Find visibility_of_element_located{locator}")
    def get_element(self, locator: tuple[str, str]) -> WebElement:
        """Find element."""
        self.logger.info("Find visible element by locator -  %s", locator)
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator),
        )

    def get_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        """Find elements."""
        self.logger.info("Find visible elements by locator -  %s", locator)
        return self.wait.until(
            expected_conditions.visibility_of_all_elements_located(locator),
        )

    @allure.step("Find and click to button {locator}")
    def click(self, locator: tuple[str, str]) -> None:
        """Click on the element with the user-like delay."""
        self.logger.info(
            "Create ActionChains and click to button founded by locator - %s",
            locator,
        )
        chains = ActionChains(self.browser)
        chains.move_to_element(
            self.get_element(locator),
        ).pause(
            1.0,
        ).click().perform()

    @allure.step("Input {text} to {locator}")
    def input_value(self, locator: tuple[str, str], text: str) -> None:
        """Enter text to the input by single key."""
        self.logger.info("Input text to %s", locator)
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for symbol in text:
            self.get_element(locator).send_keys(symbol)

    def wait_for_url_contains(self, part_of_url: str) -> None:
        """Waiter for URL."""
        self.wait.until(expected_conditions.url_contains(part_of_url))

    @allure.step("Execute js script")
    def execute_js(self, script: str, *args: Any) -> Any:
        """Execute JS script."""
        self.logger.info("Execute js script %s", script)
        return self.browser.execute_script(script, *args)

    def click_checkbox(self, checkbox: WebElement, idx: int | str = 0) -> None:
        self.execute_js(f"arguments[{idx}].click()", checkbox)

    def wait_for_condition(
        self,
        *,
        condition: Callable,
    ) -> WebDriverWait:
        return self.wait.until(condition)
