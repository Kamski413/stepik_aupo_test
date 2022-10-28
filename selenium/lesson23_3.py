from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    first_button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    x_element = browser.find_element(By.ID, 'input_value').text
    input_answer = browser.find_element(By.ID, 'answer').send_keys(calc(int(x_element)))
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    
    
finally:
    time.sleep(10)
    browser.quit()