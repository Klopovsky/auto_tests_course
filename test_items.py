import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link = "http://selenium1py.pythonanywhere.com/"

def test_exist_button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button != [] , "The button (btn-add-to-basket) not exist"