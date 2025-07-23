import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get('https://afd.calpoly.edu/web/sample-tables')

    time.sleep(3)

    # table_data = driver.find_elements(By.TAG_NAME,'td')
    #
    # print(type(table_data))
    # print(len(table_data))

    # for data in table_data:
    #     print('==== ', data.text)

    table_row_data = driver.find_elements(By.TAG_NAME, 'tr')
    print("No of rows",len(table_row_data))

    table_header_data = table_row_data[0].find_elements(By.TAG_NAME,'th')
    print("No of header columns", len(table_header_data))

    assert table_header_data[1].text == 'Date'

    table_col_data = table_row_data[1].find_elements(By.TAG_NAME, 'td')
    print("No of data columns", len(table_col_data))

    driver.close()


