import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_check_the_existence_of_add_to_bastet_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button,"Button is not found"