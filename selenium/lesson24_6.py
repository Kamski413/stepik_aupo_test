from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/cats.html')
browser.implicitly_wait(5)

try:
    button_cat = browser.find_element(By.ID, 'button').click()
finally:
    browser.quit()