import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook


def get_test_data():
    password = 'secret_sauce'

    user_data_list = [('standard_user',password),('locked_out_user',password),('problem_user',password),('performance_glitch_user',password), ('error_user',password),('visual_user',password)]

    return user_data_list

@pytest.mark.parametrize('username,password',get_test_data())
def test_param(username,password):
    base_url = 'https://www.saucedemo.com/'
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(5)
    driver.maximize_window()
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'login-button').click()
    time.sleep(5)
    driver.close()



