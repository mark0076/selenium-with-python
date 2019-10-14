from .locators import BasketPageLocators
from .locators import BasePageLocators
from .base_page import BasePage
class BasketPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
    def wait_h1_of_page(self):
        self.page_already_opened(*BasePageLocators.H1_NAME_OF_PAGE)
    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_THE_BASKET),\
            "There are some items in the basket"
    def should_basket_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET),\
            "The basket isn't empty"
        
