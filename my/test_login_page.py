import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage



def test_register_new_user(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser,link)
    page.open()
    page.go_to_register_page()
    page = LoginPage(browser,link)
    page.register_new_user()
    