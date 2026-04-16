"""Admin page E2E tests."""
from selenium.webdriver.remote.webdriver import WebDriver

from src.admin import AdminDashboardPage


def test_admin_login_logout(
    browser: WebDriver,
    base_url: str,
    admin_credentials: dict[str, str],
) -> None:
    """Login to admin page test."""
    dashboard = AdminDashboardPage(
        browser,
        base_url,
        admin_credentials,
    ).open_page()
    dashboard.is_loaded()
    dashboard.logout()
    assert dashboard.is_not_login(), "Logout didn't work"
