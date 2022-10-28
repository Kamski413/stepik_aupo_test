from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/get_attribute.html'

try:
    browser.get(link)
    treasure_pict = browser.find_element(By.CSS_SELECTOR, '#treasure')
    treasure_x = treasure_pict.get_attribute('valuex')
    input_x = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_send_key = input_x.send_keys(calc(treasure_x))
    checkbox_click = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    radiobutton_click = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    sumbit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()