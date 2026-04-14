"""Admin page."""
import allure

from src.admin.base_page import AdminBasePage


class AdminDashboardPage(AdminBasePage):
    """Admin page."""

    PATH = "administration/index.php?route=common/dashboard"

    @allure.step("Admin dashboard is loaded")
    def is_loaded(self) -> bool:
        """Method that verify the admin is successfully login."""
        self.wait_for_url_contains("dashboard")
        return True

    @allure.step("Logout from admin interface")
    def logout(self) -> None:
        """Logout method."""
        self.click(self.LOGOUT)
        self.wait_for_url_contains("login")
