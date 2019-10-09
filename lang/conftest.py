from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
        help="Choose one of the languages:"+
        " ar ca cs da de  en-gb el es fi fr it ko nl pl pt  pt-br ro ru sk uk zn-cn" )



@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    languages = "ar ca cs da de  en-gb el es fi fr it ko nl pl pt  pt-br ro ru sk uk zn-cn"
    if  language in languages:
        print("\nStart Chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages':  language})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nYour language is not supported")
        pytest.fail("Wrong Language")
    yield browser
    print("\nQuit browser")
    browser.quit()
