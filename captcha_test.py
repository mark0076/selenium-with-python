from selenium import webdriver

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element_by_css_selector('span.nowrap#input_value')
x = x_element.text
y = calc(x)
people_radio = browser.find_element_by_css_selector("input#peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

browser.find_element_by_css_selector('input.form-control').send_keys(y)
browser.find_element_by_css_selector("input#robotCheckbox").click()
browser.find_element_by_css_selector("label[for=\"robotsRule\"]").click()
browser.find_element_by_css_selector("button.btn.btn-default").click()

