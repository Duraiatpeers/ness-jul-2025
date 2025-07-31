import time

import pytest
from login_page import LoginPage

def test_valid_login(setup_browser):
    driver = setup_browser
    driver.get("https://opensource-demo.orangehrmlive.com/")

    time.sleep(10)
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Add assertion based on expected result after login
    assert "dashboard" in driver.current_url.lower()
