from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_REG = (By.ID, "id_registration-email")
    PASSWORD_1_REG = (By.ID, "id_registration-password1")
    PASSWORD_2_REG = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators():
    ADD_TO_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    ALERT_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    CART_TOTAL = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")


class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "div.basket-title.hidden-xs")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
