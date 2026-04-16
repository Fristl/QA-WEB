"""Account registration E2E tests."""
from selenium.webdriver.remote.webdriver import WebDriver

from src.shop import RegisterPage


def test_user_registration(
    browser: WebDriver,
    base_url: str,
    new_user: dict[str, str],
) -> None:
    page = RegisterPage(browser, base_url).open_page()
    page.register(**new_user)
    assert page.is_success(), f"User with {new_user} data is not registered"
