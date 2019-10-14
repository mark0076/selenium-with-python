from .locators import LoginPageLocators
from .base_page import BasePage
import time

class LoginPage(BasePage):

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "dfsf48EWSdaDDS"
        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        register_email_field.send_keys(email)
        register_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        register_password_field.send_keys(password)
        register_confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        register_confirm_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        
    def authorization_check(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON)
        