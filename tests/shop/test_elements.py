"""Component tests for UI elements."""
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.shop import BasePage
from src.shop import CategoryPage
from src.shop import ProductPage
from src.shop import RegisterPage


@pytest.mark.parametrize("page_url", ["", "en-gb/catalog/desktops"])
def test_page_elements(
    browser: WebDriver,
    base_url: str,
    page_url: str,
) -> None:
    """Verification of elements on shop's pages."""
    page = BasePage(browser, base_url, page_url).open_page()
    assert page.get_element(("id", "logo"))
    assert page.get_element(("name", "search"))
    assert page.get_element(("link text", "My Account"))
    assert page.get_element(("link text", "Shopping Cart"))
    assert page.get_element(("link text", "Checkout"))


@pytest.mark.parametrize(
    ("page_url", "category_title"),
    [
        ("en-gb/catalog/desktops", "Desktops"),
        ("en-gb/catalog/laptop-notebook", "Laptops & Notebooks"),
    ],
)
def test_catalog_page(
    browser: WebDriver,
    base_url: str,
    page_url: str,
    category_title: str,
) -> None:
    """Verification of elements on the catalog page."""
    page = CategoryPage(
        browser,
        base_url,
        page_url,
        category_title,
    ).open_page()
    assert page.is_loaded(), \
        f"Page {category_title} doesn't have correct options."


@pytest.mark.parametrize(
    ("url", "title", "price"),
    [
        ("en-gb/product/desktops/hp-lp3065", "HP LP3065", 122),
        ("en-gb/product/desktops/ipod-classic", "iPod Classic", 122),
        ("en-gb/product/smartphone/iphone", "iPhone", 123),
    ],
)
def test_product_page(
    browser: WebDriver,
    base_url: str,
    url: str,
    title: str,
    price: int,
) -> None:
    """Verification of elements on the product page."""
    page = ProductPage(browser, base_url, url, title, price).open_page()
    assert page.is_loaded(), f"Page {ProductPage} is not loaded."


def test_register_page(browser: WebDriver, base_url: str) -> None:
    """Verification of registration elements on the user page."""
    RegisterPage(browser, base_url).open_page().is_loaded()
