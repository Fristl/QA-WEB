"""Product category page."""
from typing import ClassVar

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from src.shop.base_page import ShopBasePage


class CategoryPage(ShopBasePage):
    """Product category page."""

    OPTIONS: ClassVar[set[str]] = {
        "Default",
        "Name (A - Z)",
        "Name (Z - A)",
        "Price (Low > High)",
        "Price (High > Low)",
        "Rating (Highest)",
        "Rating (Lowest)",
        "Model (A - Z)",
        "Model (Z - A)",
    }

    def __init__(
        self,
        browser: WebDriver,
        base_url: str,
        path: str,
        title: str,
    ):
        super().__init__(browser, base_url, path)
        self.title = title

    def is_loaded(self) -> bool:
        """Method that verify the category is shown."""
        self.wait_for_visible_element((By.XPATH, f"//h2[text()='{self.title}']"))
        self.wait_for_visible_element((By.CLASS_NAME, "product-thumb"))
        self.wait_for_visible_element((By.ID, "input-sort"))
        sort_dropdown = self.get_element((By.ID, "input-sort"))
        select = Select(sort_dropdown)
        actual_options = {option.text for option in select.options}
        return actual_options == self.OPTIONS
