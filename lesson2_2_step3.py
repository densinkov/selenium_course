from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открытие страницы
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
finally:
    time.sleep(10)
    browser.quit()