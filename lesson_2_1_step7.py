from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

# Математическая функция
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открытие страницы
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск элемента-картинки
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")

    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввод ответа в текстовое поле
    input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input.send_keys(y)

    # Отметить checkbox
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

    # Выбрать radiobutton
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()
    
    # Нажать на кнопку Submit
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    
    browser.quit()