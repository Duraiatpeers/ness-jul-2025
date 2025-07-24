import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_demo1():
    base_url = 'https://jqueryui.com/droppable'
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(3)
    driver.maximize_window()

    driver.switch_to.frame(0)

    element1 = driver.find_element(By.ID,'draggable')
    element2 = driver.find_element(By.ID, 'droppable')

    # ActionChains(driver)\
    #     .drag_and_drop(element1,element2)\
    #     .perform()

    ActionChains(driver)\
        .move_to_element(element1)\
        .click_and_hold()\
        .move_to_element(element2)\
        .release() \
        .click_and_hold() \
        .move_by_offset(30,60) \
        .release() \
        .perform()

    time.sleep(5)

    driver.close()
