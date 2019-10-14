from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nStart Chrome browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser")
    browser.quit()