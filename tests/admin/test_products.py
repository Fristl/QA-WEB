"""Admin product E2E tests."""
from selenium.webdriver.remote.webdriver import WebDriver

from src.admin.product_form_page import AdminProductFormPage
from src.admin.products_page import AdminProductsPage


def test_admin_add_new_product(
    browser: WebDriver,
    base_url: str,
    admin_credentials: dict[str, str],
    unique_product_name: str,
    unique_seo: str,
) -> None:
    products = AdminProductsPage(
        browser,
        base_url,
        admin_credentials,
    ).open_page()

    products.click_add()
    form = AdminProductFormPage(browser, base_url, admin_credentials)
    form.fill_and_save(
        name=unique_product_name,
        meta_title=f"Meta {unique_product_name}",
        model="QA-TEST-MODEL",
        seo_keyword=unique_seo,
    )

    assert "Success" in products.success_text()
    AdminProductsPage(
        browser,
        base_url,
        admin_credentials,
    ).open_page()
    products.filter_by_name(unique_product_name)
    assert products.is_product_present(unique_product_name), \
        "Product not found in the list after save"


def test_admin_delete_product(
    browser: WebDriver,
    base_url: str,
    admin_credentials: dict[str, str],
    unique_product_name: str,
    unique_seo: str,
) -> None:
    # Create product
    products = AdminProductsPage(
        browser,
        base_url,
        admin_credentials,
    ).open_page()

    products.click_add()
    form = AdminProductFormPage(browser, base_url, admin_credentials)
    form.fill_and_save(
        name=unique_product_name,
        meta_title=f"Meta {unique_product_name}",
        model="QA-TEST-MODEL",
        seo_keyword=unique_seo,
    )
    assert "Success" in products.success_text()

    AdminProductsPage(
        browser,
        base_url,
        admin_credentials,
    ).open_page()
    # Delete product
    products.delete_by_name(unique_product_name)
    assert "Success" in products.success_text()
    assert products.no_results_text() == "No results!", \
        "Product still present after deletion"
