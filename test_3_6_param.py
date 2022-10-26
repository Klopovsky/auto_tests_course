import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



list_num = ["895", "896", "897", "898", "899", "903", "904", "905"]

@pytest.mark.parametrize('number', list_num)
class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser,number):
        link = f"https://stepik.org/lesson/236{number}/step/1"
        browser.get(link)
        wait = WebDriverWait(browser, 10)
        browser.implicitly_wait(10)
        input = browser.find_element(By.CSS_SELECTOR, "textarea")
        input.send_keys(str(math.log(int(time.time()))))
        button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button.click()
        wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".smart-hints__hint")))
        answer = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        assert answer.text == "Correct!"

 