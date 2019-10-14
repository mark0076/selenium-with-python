import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage 
from .pages.login_page import LoginPage
import time


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser,link)
        page.open()
        page.register_new_user()
        page.authorization_check()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_product_to_basket()
        #page.solve_quiz_and_get_code()
        page.check_correct_name_in_the_basket()
        page.check_correct_price_in_the_basket()
    
    def test_user_cant_see_success_message(self,browser): 
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
        
class TestGuestAddToBasketFromProductPage():        
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser,link)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser,link)
        page.wait_h1_of_page()
        page.should_not_be_items_in_the_basket()
        page.should_basket_be_empty()
    @pytest.mark.need_review    
    def test_guest_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_product_to_basket()
        #page.solve_quiz_and_get_code()
        page.check_correct_name_in_the_basket()
        page.check_correct_price_in_the_basket()
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        