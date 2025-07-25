import time

from selenium import webdriver

from day3.DataConfig.BaseConfig import BaseConfig
from day3.Pages.LoginPage import LoginPage
from day3.DataConfig.LoginData import LoginData

driver = ''
if BaseConfig.BROWSER == 'Chrome':
    driver = webdriver.Chrome()
    driver.get(BaseConfig.BASE_URL)
time.sleep(5)


class TestLogin:

    def test_invalid_login(self):
        global driver
        driver.maximize_window()
        driver.implicitly_wait(BaseConfig.DEFAULT_TIMEOUT)
        login_page = LoginPage(driver)
        login_page.invalid_login(LoginData.INVALID_USERNAME,LoginData.INVALID_PASSWORD)
        time.sleep(5)
        assert login_page.check_error_msg_displayed()
        assert login_page.get_error_msg() == 'Invalid credentials'



    def test_valid_login(self):
        login_page = LoginPage(driver)
        dboardpage = login_page.valid_login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)
        assert dboardpage.get_browser_title() == 'OrangeHRM'
        assert 'dashboard' in dboardpage.get_browser_url()





