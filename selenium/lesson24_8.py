from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math 
import time


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
wait = WebDriverWait(browser, 13)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # min_prince = browser.find_element(By.ID, 'price')
    book_button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    book_button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    submit_button = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    x = x_element.text
    y = calc(int(x))
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()