import time

import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

def test_check2():


    # Create Edge options
    options = Options()
    options.add_argument("--start-maximized")
    options.set_capability("browserName", "MicrosoftEdge")  # W3C capability
    options.set_capability("platformName", "Windows 10")  # Use ANY for generic platform

    # Remote WebDriver with Selenium Grid
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",  # No /wd/hub in Selenium 4.34.0
        options=options
    )

    # Open a test website
    driver.get("https://www.google.com")
    print("Title:", driver.title)

    time.sleep(30)
    driver.quit()
