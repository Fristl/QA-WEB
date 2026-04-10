"""Admin page E2E tests."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .conftest import wait_for_by
from .conftest import wait_for_contains_url


def test_admin_login_logout(
    browser: WebDriver,
    base_url: str,
    admin_credentials: dict[str, str],
) -> None:
    """Login to admin page test."""
    browser.get(f"{base_url}/administration")

    wait_for_by(
        browser,
        by=By.ID,
        value="input-username",
    ).send_keys(
        admin_credentials["username"],
    )
    wait_for_by(
        browser,
        by=By.ID,
        value="input-password",
    ).send_keys(
        admin_credentials["password"],
    )
    wait_for_by(browser, by=By.XPATH, value="//button[@type='submit']").click()

    wait_for_contains_url(browser, url_contains="dashboard")
    assert "dashboard" in browser.current_url.lower()

    wait_for_by(browser, by=By.ID, value="nav-logout").click()

    wait_for_contains_url(browser, url_contains="login")
    assert "login" in browser.current_url.lower()
