import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options  # ✅ Use Firefox options

def test_check2():
    # Create Firefox options
    options = Options()
    options.set_capability("browserName", "firefox")       # ✅ Must match node stereotype
    options.set_capability("platformName", "Windows 10")   # ✅ Use actual platform from node info

    # Remote WebDriver with Selenium Grid
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",  # ✅ Correct for Selenium 4.34.0
        options=options
    )

    # Open a test website
    driver.get("https://www.microsoft.com")
    print("Title:", driver.title)

    time.sleep(30)
    driver.quit()
