import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_demo1():
    base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(3)
    driver.maximize_window()
    username_field = driver.find_element(locate_with(By.NAME,'username').above({By.NAME:'password'}))
    username_field.send_keys('Admin')

    time.sleep(3)

    password_field = driver.find_element(locate_with(By.NAME, 'password').below({By.NAME: 'username'}))
    password_field.send_keys('admin123')

    time.sleep(3)

    driver.find_element(By.XPATH,'//button').submit()

    time.sleep(3)
    driver.close()