import pytest
from selenium import webdriver

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()  # or Firefox, Edge, etc.
    driver.maximize_window()
    yield driver
    driver.quit()
