import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class Test_Demo:
    @pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
    def test_open_example_com(browser):
        if browser == "chrome":
            options = ChromeOptions()
            options.set_capability("browserName", "chrome")
        elif browser == "firefox":
            options = FirefoxOptions()
            options.set_capability("browserName", "firefox")
        elif browser == "edge":
            options = EdgeOptions()
            options.set_capability("browserName", "MicrosoftEdge")  # Important: must match Grid
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Common platform name (optional, but can help match node)
        options.set_capability("platformName", "Windows 10")

        # Launch remote browser
        driver = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=options
        )

        driver.get("https://www.example.com")
        print(f"[{browser.upper()}] Title: {driver.title}")

        time.sleep(30)
        driver.quit()
