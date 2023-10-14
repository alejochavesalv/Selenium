"""
Test Case
-------------------------------------------------------------
1) Open Web Browser(Chrome/firefox/Edge).
2) Open URL  https://opensource-demo.orangehrmlive.com/
3) Enter username  (Admin).
4) Enter password  (admin123).   
5) Click on Login.
6) Verify module
7) close browser
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Edge()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.NAME, 'username').clear()
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.XPATH, '//*[@type="submit"]').click()

try:
    act_module = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
    if act_module == 'Dashboard':
        print('Test passed')
    else:
        print('Test failed')
except NoSuchElementException as error:
    print('Test failed')