import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver.implicitly_wait(10)

    driver.get('https://opensource-demo.orangehrmlive.com')
    time.sleep(3)

    driver.find_element(By.XPATH,'//form/div[1]//input').send_keys('Admin')
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,'form > div:nth-child(3) input').send_keys('admin123')
    time.sleep(2)

    driver.find_element(By.XPATH,'//form//div/child::button').click()
    #time.sleep(4)

    #assert driver.current_url =='https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'

    # time.sleep(4)

    wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
    wait.until(ec.presence_of_element_located((By.XPATH,'//header//ul[@data-v-c286b6e5]/li')))

    driver.find_element(By.XPATH,'//header//ul[@data-v-c286b6e5]/li').click()

    time.sleep(4)

    driver.close()


