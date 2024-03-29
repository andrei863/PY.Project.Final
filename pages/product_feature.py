

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    LOGIN_PAGE_URL = "https://www.saucedemo.com/v1/"
    INPUT_EMAIL = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCT_PAGE_URL = "https://www.saucedemo.com/v1/inventory.html"
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn_primary")
    SHOPPING_CART = (By.CLASS_NAME, "fa-layers-counter")
    SHOPPING_BUTTON = (By.ID, "shopping_cart_container")
    CART_PAGE_URL = "https://www.saucedemo.com/v1/cart.html"
    CHECKOUT_BUTTON = (By.CLASS_NAME, "btn_action ")
    CHECKOUT_PAGE_URL = "https://www.saucedemo.com/v1/checkout-step-one.html"


    def open_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def verify_login_page_url(self):
        assert self.driver.current_url == self.LOGIN_PAGE_URL

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.find(self.INPUT_LOGIN_BUTTON).click()

    def verify_product_page_url(self):
        assert self.driver.current_url == self.PRODUCT_PAGE_URL

    def click_add_to_cart(self):
        self.find(self.BUTTON_ADD_TO_CART).click()

    def verify_no_empty_cart(self, expected):
        assert expected in self.find(self.SHOPPING_CART).text


    def click_shopping_cart(self):
        self.find(self.SHOPPING_BUTTON).click()


    def verify_shopping_cart_page(self):
        assert self.driver.current_url == self.CART_PAGE_URL


    def click_check_out_button(self):
        self.find((self.CHECKOUT_BUTTON)).click()

    def verify_checkout_page_url(self):
        assert self.driver.current_url == self.CHECKOUT_PAGE_URL

