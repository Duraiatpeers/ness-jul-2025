import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    time.sleep(3)

    driver.find_element(By.XPATH,'//form/div[1]//input').send_keys('Admin')
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,'form > div:nth-child(3) input').send_keys('admin123')
    time.sleep(2)

    driver.find_element(By.XPATH,'//form//div/child::button').click()
    time.sleep(4)

    assert driver.current_url =='https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
    time.sleep(3)


    driver.close()


