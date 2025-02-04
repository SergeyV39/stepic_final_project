from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_not_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), 'Basket is not empty'

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), 'Basket is not empty'
