from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/math.html')

try:
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)
    check_box = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check_box.click()
    radio_button = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_button.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()
    
finally:
    time.sleep(10)
    browser.quit() 