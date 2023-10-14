"""
Assignment
----------------------------------------------------------------------------------------------
1) Open Web Browser(Chrome/firefox/IE).
2) Open URL  https://admin-demo.nopcommerce.com/login
3) Provide Email  (admin@yourstore.com).
4) Provide password  (admin).   
5) Click on Login.
6) Capture title of the dashboad page.(Actual title)
7) Verify title of the page: "Dashboard / nopCommerce administration" (Expected)
8) close browser
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Edge()
driver.get('https://admin-demo.nopcommerce.com/login')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID, 'Email').clear()
driver.find_element(By.ID, 'Email').send_keys('admin@yourstore.com')
driver.find_element(By.ID, 'Password').clear()
driver.find_element(By.ID, 'Password').send_keys('admin')
driver.find_element(By.XPATH, '//*[@type="submit"]').click()

try:
    act_title = driver.title
    act_module = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/h1').text
    if act_title == 'Dashboard / nopCommerce administration' and act_module == 'Dashboard':
        print('Test passed')
    else:
        print('Test failed')
except NoSuchElementException as error:
    print('Test failed')

