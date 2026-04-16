"""Component tests for UI elements."""
from selenium.webdriver.remote.webdriver import WebDriver

from src.admin import AdminLoginPage


def test_admin_login(browser: WebDriver, base_url: str) -> None:
    """Verification of login elements on the admin page."""
    login = AdminLoginPage(browser, base_url).open_page()
    assert login.is_loaded(), "Admin login page is not loaded"
