import pytest
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

# marker annotation to set the order

# @pytest.mark.order(2)
# @pytest.mark.smoke
def test_check2():
    driver.get('http://amazon.com')
    assert 'India' in driver.title

# @pytest.mark.order(1)
# @pytest.mark.regression
def test_check1():
    driver.get('http://ebay.com')
    assert 'Cars' in driver.title

# @pytest.mark.skip
# @pytest.mark.xfail
def test_demo201(self):
    assert "Smoke" in ["Regression","Security"]