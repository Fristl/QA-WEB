"""Admin product page."""
from selenium.webdriver.common.by import By

from src.admin.base_page import AdminBasePage


class AdminProductFormPage(AdminBasePage):
    """Admin product page."""

    # Tabs
    TAB_GENERAL = (By.XPATH, "//a[@href='#tab-general']")
    TAB_DATA = (By.XPATH, "//a[@href='#tab-data']")
    TAB_SEO = (By.XPATH, "//a[@href='#tab-seo']")
    INPUT_SEO_KEYWORD = (By.NAME, "product_seo_url[0][1]")

    # General tab fields
    INPUT_NAME = (By.ID, "input-name-1")
    INPUT_META_TITLE = (By.ID, "input-meta-title-1")

    # Data tab fields
    INPUT_MODEL = (By.ID, "input-model")

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and @form='form-product']",
    )

    def fill_and_save(
        self,
        name: str,
        meta_title: str,
        model: str,
        seo_keyword: str,
    ) -> None:
        """Fill in the necessary data for product creation."""
        # General
        self.click(self.TAB_GENERAL)
        self.input_value(self.INPUT_NAME, name)
        self.input_value(self.INPUT_META_TITLE, meta_title)

        # Data
        self.click(self.TAB_DATA)
        self.input_value(self.INPUT_MODEL, model)

        # SEO
        self.click(self.TAB_SEO)
        self.input_value(self.INPUT_SEO_KEYWORD, seo_keyword)

        # Save
        self.click(self.SAVE_BUTTON)
