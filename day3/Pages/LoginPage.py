from selenium import webdriver
from selenium.webdriver.common.by import By
from LPLocators import LPLocators
from day3.DashboardPage import DashboardPage


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_loc_byname = LPLocators.username_loc_byname
        self.password_loc_byname = LPLocators.password_loc_byname
        self.loginbtn_loc_byxpath = LPLocators.loginbtn_loc_byxpath
        self.error_msg_byxpath = LPLocators.error_msg_byxpath

    def enter_username(self,username):
        driver = self.driver
        driver.find_element(By.NAME,self.username_loc_byname).send_keys(username)

    def enter_password(self,password):
        driver = self.driver
        driver.find_element(By.NAME,self.password_loc_byname).send_keys(password)

    def click_loginbtn(self):
        driver = self.driver
        driver.find_element(By.XPATH,self.loginbtn_loc_byxpath).click()

    def get_error_msg(self):
        driver = self.driver
        return driver.find_element(By.XPATH,self.error_msg_byxpath).text

    def check_error_msg_displayed(self):
        driver = self.driver
        return driver.find_element(By.XPATH, self.error_msg_byxpath).is_displayed()


    def valid_login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_loginbtn()
        return DashboardPage(self.driver)

    def invalid_login(self,inv_username,inv_password):
        self.enter_username(inv_username)
        self.enter_password(inv_password)
        self.click_loginbtn()
