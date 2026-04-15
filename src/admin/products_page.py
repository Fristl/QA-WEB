"""Admin product page."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.admin.base_page import AdminBasePage


class AdminProductsPage(AdminBasePage):
    """Admin product page."""

    PATH = "administration/index.php?route=catalog/product"

    MENU_CATALOG = (By.ID, "menu-catalog")
    LINK_PRODUCTS = (By.XPATH, "//a[text()='Products']")
    ADD_BUTTON = (By.CLASS_NAME, "fa-plus")
    DELETE_BUTTON = (By.CLASS_NAME, "fa-trash-can")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    NO_RESULTS = (By.XPATH, "//*[@id='form-product']/div[1]/table/tbody/tr/td")

    FILTER_NAME = (By.ID, "input-name")
    FILTER_BUTTON = (By.XPATH, "//*[@id='button-filter']/i")

    TABLE = (By.CSS_SELECTOR, "table.table")
    TABLE_ROWS = (By.CSS_SELECTOR, "table.table tbody tr")
    ROW_NAME_CELL = (By.CSS_SELECTOR, "td:nth-child(3)")
    ROW_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    def get_table(self) -> None:
        self.get_element(self.TABLE)

    @allure.step("Click to button for adding product to cart")
    def click_add(self) -> None:
        """Add new product."""
        self.click(self.ADD_BUTTON)

    @allure.step("Delete product with name '{name}'")
    def delete_by_name(self, name: str) -> None:
        """Delete product."""
        self.filter_by_name(name)
        self.get_element(self.TABLE)
        rows = self.get_elements(self.TABLE_ROWS)
        checkbox = WebDriverWait(rows[0], 5).until(
            expected_conditions.visibility_of_element_located(
                (self.ROW_CHECKBOX[0], self.ROW_CHECKBOX[1]),
            ),
        )
        self.click_checkbox(checkbox)
        self.click(self.DELETE_BUTTON)
        alert = self.browser.switch_to.alert
        alert.accept()
        self.get_elements(self.SUCCESS_ALERT)
        self.success_text_is_hidden()

    @allure.step("Set products filter by name - '{name}'")
    def filter_by_name(self, name: str) -> None:
        """Filter products."""
        self.input_value(self.FILTER_NAME, name)
        self.click(self.FILTER_BUTTON)

    @allure.step("Check if product with name {name} is present")
    def is_product_present(self, name: str) -> bool:
        """Method that verify the product is shown."""
        self.get_element(self.TABLE)
        # rows = self.get_elements(self.TABLE_ROWS)
        rows = self.get_elements(self.TABLE_ROWS)
        for row in rows:
            if WebDriverWait(row, 5).until(
                expected_conditions.visibility_of_element_located(
                    (self.ROW_NAME_CELL[0], self.ROW_NAME_CELL[1]),
                ),
            ).text.split()[0] == name:
                return True
        return False

    @allure.step("Find success alert text")
    def success_text(self) -> str:
        """Success message."""
        return self.get_element(self.SUCCESS_ALERT).text

    def success_text_is_hidden(self) -> None:
        """Success message."""
        self.wait.until(
            expected_conditions.invisibility_of_element_located(
                self.SUCCESS_ALERT,
            ),
        )

    @allure.step("Find no results alert text")
    def no_results_text(self) -> str:
        """No results."""
        return self.get_element(self.NO_RESULTS).text
