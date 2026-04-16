"""Conftest."""
import logging
import platform
import random
import string
import uuid
from typing import Any
from typing import Generator

import allure
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
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser: Any) -> None:
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
        if platform.system() == "Windows":
            chrome_type = ChromeType.GOOGLE
        else:
            chrome_type = ChromeType.CHROMIUM
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        return Chrome(
            service=ChromeService(
                ChromeDriverManager(chrome_type=chrome_type).install(),
            ),
            options=chrome_options,
        )

    if browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        return Firefox(
            service=FirefoxService(
                executable_path="/usr/bin/geckodriver",
            ),
            options=firefox_options,
        )

    if browser_name == "safari":
        safari_options = SafariOptions()
        return Safari(
            service=SafariService(),
            options=safari_options,
        )
    return None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Function,
) -> Generator[None, Any, None]:
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot = driver.get_screenshot_as_png()  # type: ignore[attr-defined]
            allure.attach(
                screenshot,
                name=f"Screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG,
            )


@pytest.fixture
def browser(request: Any) -> Generator[WebDriver, Any, None]:
    """Select browser."""
    browser_name = request.config.getoption("--browser")
    driver = create_browser(browser_name)
    if driver is None:
        msg = f"Browser '{browser_name}' is not supported"
        raise ValueError(msg)
    driver.test_name = request.node.originalname  # type: ignore[attr-defined]
    driver.log_level = logging.INFO  # type: ignore[attr-defined]

    yield driver
    driver.quit()


@pytest.fixture
def base_url(request: Any) -> str:
    """Base URL."""
    return request.config.getoption("--base_url")


@pytest.fixture
def admin_credentials() -> dict[str, str]:
    return {
        "username": "user",
        "password": "bitnami",
    }


@pytest.fixture
def unique_email() -> str:
    return f"qa_{uuid.uuid4().hex[:8]}@example.com"


@pytest.fixture
def unique_product_name() -> str:
    return f"{uuid.uuid4().hex[:6]}"


@pytest.fixture
def random_string(length: int = 6) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))  # noqa: S311


@pytest.fixture
def random_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits + "!@#"
    return "".join(random.choices(chars, k=length))  # noqa: S311


@pytest.fixture
def unique_seo() -> str:
    return uuid.uuid4().hex[:6]


@pytest.fixture
def new_user(
    random_string: str,
    unique_email: str,
    random_password: str,
) -> dict[str, str]:
    return {
        "firstname": random_string,
        "lastname": random_string,
        "email": unique_email,
        "password": random_password,
    }
