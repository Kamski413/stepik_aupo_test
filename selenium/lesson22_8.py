from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

try:
    name_input = browser.find_element(By.NAME, 'firstname').send_keys('Dima')
    last_name_input = browser.find_element(By.NAME, 'lastname').send_keys('Aben')
    email_input = browser.find_element(By.NAME, 'email').send_keys('test@test.com')
    with open("test.txt", "w") as file:
        content = file.write("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file_download = browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    
finally:
    time.sleep(10)
    browser.quit()