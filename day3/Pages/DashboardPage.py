from selenium import webdriver
from selenium.webdriver.common.by import By
from day3.Locators.LPLocators import LPLocators

class DashboardPage:

    def __init__(self,driver):
        self.driver = driver

    def get_browser_title(self):
        return self.driver.title

    def get_browser_url(self):
        return self.driver.current_url

