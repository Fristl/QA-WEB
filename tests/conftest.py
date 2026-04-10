"""Conftest."""
from typing import Any
from typing import Callable
from typing import Generator

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ChromeService
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import FirefoxService
from selenium.webdriver import Safari
from selenium.webdriver import SafariOptions
from selenium.webdriver import SafariService
from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser) -> None:
    """
    Custom command line parameters for running test,
    by default Chrome driver.
    """
    parser.addoption(
        "--base_url",
        action="store",
        default="http://localhost:8080",
        help="Base URL of OpenCart",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )


def create_browser(browser_name: str) -> WebDriver | None:
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        return Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options,
        )

    if browser_name == "firefox":
        firefox_options = FirefoxOptions()
        return Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options,
        )

    if browser_name == "safari":
        safari_options = SafariOptions()
        return Safari(
            service=SafariService(),
            options=safari_options,
        )
    return None




@pytest.fixture
def browser(request) -> Generator[WebDriver, Any, None]:
    """Select browser."""
    browser_name = request.config.getoption("--browser")
    driver = create_browser(browser_name)
    if driver is None:
        msg = f"Browser '{browser_name}' is not supported"
        raise ValueError(msg)
    yield driver
    driver.quit()


@pytest.fixture
def base_url(request) -> str:
    """Base URL."""
    return request.config.getoption("--base_url")


def wait_for_element(
    driver: WebDriver,
    by: ByType,
    value: str,
    timeout: int = 5,
) -> WebElement:
    """Explicit waiter."""
    return WebDriverWait(
        driver,
        timeout,
    ).until(
        expected_conditions.visibility_of_element_located((by, value)),
    )


def wait_for_by(
    driver: WebDriver,
    *,
    by: ByType | str,
    value: str,
    timeout: int = 5,
) -> WebElement:
    return WebDriverWait(
        driver,
        timeout,
    ).until(
        expected_conditions.visibility_of_element_located((by, value)),
    )


def wait_for_condition(
    driver: WebDriver,
    *,
    condition: Callable,
    timeout: int = 5,
) -> WebDriverWait:
    return WebDriverWait(driver, timeout).until(condition)


def wait_for_contains_url(
    driver: WebDriver,
    *,
    url_contains: str,
    timeout: int = 5,
) -> bool:
    return WebDriverWait(
        driver,
        timeout,
    ).until(
        expected_conditions.url_contains(url_contains),
    )


@pytest.fixture
def admin_credentials() -> dict[str, str]:
    return {
        "username": "user",
        "password": "bitnami",
    }
