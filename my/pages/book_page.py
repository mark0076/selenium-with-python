from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
import time
class ProductPage(BasePage):    

    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)
    def click_add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()        
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def check_correct_name_in_the_basket(self):
        time.sleep(2)
        item_in_the_page = self.browser.find_element(*ProductPageLocators.NAME_OF_ITEM_IN_THE_PAGE)
        item_in_the_basket = self.browser.find_element(*BasketPageLocators.NAME_OF_ITEM_IN_THE_BASKET)

        assert (item_in_the_page.text == item_in_the_basket.text)
            
    def check_correct_price_in_the_basket(self):
        time.sleep(2)
        price_of_item_in_the_page = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_THE_PAGE)
        price_of_item_in_the_basket = self.browser.find_element(
            *BasketPageLocators.PRODUCT_PRICE_IN_THE_BASKET)
        assert (price_of_item_in_the_page.text == price_of_item_in_the_basket.text)
        time.sleep(6)
        
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
           
            
    def should_not_message_dissapear(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should dissaper"
        
    