from selenium import webdriver
from selenium.webdriver.common.by import By
import math 
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    moved_button = browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    second_browser = browser.window_handles[1]
    browser.switch_to.window(second_browser)
    x_element = browser.find_element(By.ID, 'input_value').text
    input_answer = browser.find_element(By.ID, 'answer').send_keys(calc(int(x_element)))
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    
    
finally:
    time.sleep(10)
    browser.quit()