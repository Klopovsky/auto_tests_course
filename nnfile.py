from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("rrran")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("Ivan@rrr.ty")

    element = browser.find_element(By.CSS_SELECTOR, "#file")
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
