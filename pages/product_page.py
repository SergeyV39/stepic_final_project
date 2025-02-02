from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.click_add_to_cart_button()
        self.solve_quiz_and_get_code()
        self.message_product_in_cart()
        self.price_cart_equal_price_product()

    def click_add_to_cart_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUTTON)
        add_button.click()

    def message_product_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text == self.browser.find_element(
            *ProductPageLocators.ALERT_SUCCESS).text, 'In cart wrong product'

    def price_cart_equal_price_product(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(
            *ProductPageLocators.CART_TOTAL).text, 'the prices in the cart and the product are different'
