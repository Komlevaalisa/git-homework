from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим ВСЕ поля ввода на странице
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Заполняем каждое поле
    for element in elements:
        element.send_keys("Мой ответ")

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()