import allure
import pytest


def get_test_data():
    user_data_list = [('Admin','admin123'),('Tom','welcome123')]
    return user_data_list


@allure.title("First testcase")
@allure.title("Login Test with Valid Credentials")
@allure.description("This test verifies login functionality for valid users.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("team", "QA Team")
@allure.tag("regression", "smoke")
@allure.epic("User Management")
@allure.feature("Login")
@allure.story("Valid user login")
@allure.issue("BUG-101", "Login button not working")
@allure.testcase("TC-202", "Test Case in TestRail")
@pytest.mark.parametrize('username,password',get_test_data())
def test_param(username,password):
    print(username)
    print(password)
