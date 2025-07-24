import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_demo1():
    base_url = 'https://ebay.com'
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(3)
    driver.maximize_window()

    driver.execute_script("document.getElementById('gh-ac').value='Samsung'")
    time.sleep(5)

    driver.execute_script("document.getElementById('gh-search-btn').click()")

    time.sleep(5)

    driver.close()
