from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    first_number = browser.find_element(By.CSS_SELECTOR, '#num1').text
    # symbol = browser.find(By.CSS_SELECTOR, 'h2 > span:nth-child(3)').text
    second_number = browser.find_element(By.CSS_SELECTOR, '#num2').text
    sum_of_numbers = (int(first_number) + int(second_number))
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_value(f'{sum_of_numbers}')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    
finally:
    time.sleep(10)
    browser.quit()