"""Admin page."""
from .base_page import BasePage


class AdminDashboardPage(BasePage):
    """Admin page."""

    PATH = "administration/index.php?route=common/dashboard"

    def is_loaded(self) -> bool:
        """Method that verify the admin is successfully login."""
        self.wait_for_url_contains("dashboard")
        return True

    def logout(self) -> None:
        """Logout method."""
        self.click(self.LOGOUT)
        self.wait_for_url_contains("login")
