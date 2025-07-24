import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_demo1():
    base_url = 'https://javascript.info/alert-prompt-confirm'
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(3)
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR,'div#pbrqczhaig div:nth-child(1) > a').click()
    time.sleep(3)

    new_alert = driver.switch_to.alert
    print('Alert text : ',new_alert.text)

    time.sleep(5)
    new_alert.accept()

    driver.close()