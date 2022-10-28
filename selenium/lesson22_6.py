from re import sub
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'
browser.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    calc_input = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(calc(int(x_element))))
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true)", robot_radiobutton)
    robot_radiobutton.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
    submit_button.click()
    
finally:
    time.sleep(10)
    browser.quit()
