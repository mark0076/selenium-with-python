import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser,link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser,link)
    page.wait_h1_of_page()
    page.should_not_be_items_in_the_basket()
    page.should_basket_be_empty()
    
    