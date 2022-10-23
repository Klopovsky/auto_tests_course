import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):

    def registr(self, link):
        #return_text = "None"
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            input1 = browser.find_element(
                By.CSS_SELECTOR, ".first_block .form-control.first")
            input1.send_keys("111")
            input2 = browser.find_element(
                By.CSS_SELECTOR, ".first_block .form-control.second")
            input2.send_keys("222")
            input3 = browser.find_element(
                By.CSS_SELECTOR, ".first_block .form-control.third")
            input3.send_keys("333")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            return_text = welcome_text_elt.text
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        finally:
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()
            return return_text

    def test_site1(self):

        self.assertEqual("Congratulations! You have successfully registered!", self.registr(
            "http://suninjuly.github.io/registration1.html"), "Error for register")

    def test_site2(self):
        self.assertEqual("Congratulations! You have successfully registered!", self.registr(
            "http://suninjuly.github.io/registration2.html"), "Error for register")


if __name__ == "__main__":
    unittest.main()
