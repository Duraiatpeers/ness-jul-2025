import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = ''

@pytest.fixture()
def setup():
    global driver
    base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(3)
    driver.maximize_window()
    yield
    driver.quit()

def test_demo1(setup):

    driver = webdriver.Chrome()


    print('Current window',driver.current_url)
    print('Current window handle : ',driver.current_window_handle)

    main_window = driver.window_handles[0]

    driver.find_element(By.PARTIAL_LINK_TEXT,'OrangeHRM').click()
    time.sleep(3)
    print('Current window', driver.current_url)

    child_window = driver.window_handles[1]
    time.sleep(3)

    driver.switch_to.window(child_window)
    print('Current window',driver.current_url)

    print('Current window handle : ', driver.current_window_handle)
    time.sleep(3)

    driver.find_element(By.XPATH,"//a[@href='/en/contact-sales']/button").click()
    time.sleep(5)

