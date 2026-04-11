"""Shop pages."""

from .base_page import BasePage
from .category_page import CategoryPage
from .create_account_page import RegisterPage
from .home_page import HomePage
from .product_page import ProductPage


__all__ = (
    "BasePage",
    "CategoryPage",
    "HomePage",
    "ProductPage",
    "RegisterPage",
)
