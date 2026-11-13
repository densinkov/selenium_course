from selenium import webdriver
from selenium.webdriver.common.By import By
import time
import math

# Математическая функция
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открытие страницы
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитаем математическую функцию от x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    # Ввод ответа в текстовое поле
    calc_input = browser.find_element(By_ID, "#answer")
    calc_input.send_keys(y)

finally:
    time.sleep(10)

    browser.quit()

    

