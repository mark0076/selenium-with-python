from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR,"button.btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_ITEM_IN_THE_PAGE = (By.CSS_SELECTOR,"div.col-sm-6.product_main>h1")
    PRODUCT_PRICE_IN_THE_PAGE = (By.CSS_SELECTOR,"div>p.price_color")
    
    

class BasketPageLocators():
    PRODUCT_PRICE_IN_THE_BASKET = (By.CSS_SELECTOR,"div.alertinner>p>strong")
    NAME_OF_ITEM_IN_THE_BASKET = (By.CSS_SELECTOR,"div.alertinner>strong:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div#messages>div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")
    EMPTY_BASKET =(By.CSS_SELECTOR,"div#content_inner>p")
    EMPTY_BASKET_AFTER_DELETED_ITEMS =(By.CSS_SELECTOR,"div.alert.alert-safe.alert-noicon.alert-info.fade.in>div.alertinner>p")
    ITEMS_IN_THE_BASKET = (By.CSS_SELECTOR,"div.basket-title.hidden-xs")
    
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR,"#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,"span.btn-group")
    H1_NAME_OF_PAGE = (By.CSS_SELECTOR,"div.page-header.action>h1")
    
class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR,"form#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR,"form#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[name=\"login-username\"]")
    LOGIN_PASSWORD =(By.CSS_SELECTOR, "input[name=\"login-password\"]")
    LOGIN_BUTTON =(By.CSS_SELECTOR, "button[name=\"login_submit\"]")
    FORGOT_PASSWORD_LINK =(By.XPATH,"//a[text() =\"I've forgotten my password\"]")
    REGISTRATION_EMAIL =(By.CSS_SELECTOR, "input[name=\"registration-email\"]")
    REGISTRATION_PASSWORD =(By.CSS_SELECTOR, "input[name=\"registration-password1\"]")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name=\"registration-password2\"]")
    REGISTER_BUTTON =(By.CSS_SELECTOR, "button[name=\"registration_submit\"]")
    LOGIN_OR_REGISTER_TAB = (By.CSS_SELECTOR,"ul.breadcrumb >li.active")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
    