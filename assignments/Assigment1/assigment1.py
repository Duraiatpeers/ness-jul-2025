import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_assigment1():
    base_url = 'https://angular-university.io/'
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(5)
    driver.maximize_window()
    my_courses_link = driver.find_element(By.XPATH,'//span[normalize-space()="My Courses"]')
    my_courses_link.click()
    time.sleep(5)
    my_courses_title = driver.find_element(By.XPATH, '//p[normalize-space()="My Courses"]')
    assert my_courses_title.text == 'My Courses'
    beginner_courses_link = driver.find_element(By.XPATH, '//div[@class="card card-course course-id-1 hoverable"]')
    beginner_courses_link.click()
    time.sleep(10)
    beginner_courses_helicopter_view_option = driver.find_element(By.XPATH,'//a[normalize-space()="Angular for Beginners - Helicopter View"]')
    assert beginner_courses_helicopter_view_option.is_displayed();
    time.sleep(10)
    checkBox_helicopter_view = driver.find_element(By.XPATH, '//tbody/tr[1]/td[1]/lesson-viewed-checkbox[1]/checkbox[1]')
    checkBox_helicopter_view.click()
    time.sleep(10)
    info_box= driver.find_element(By.XPATH, '//div[@class="messages messages-info"]')
    assert info_box.is_displayed();
    assert info_box.text == 'Information\nLogin using Github (or email / password) for marking lessons as viewed.'
