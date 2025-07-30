import allure
import pytest


def get_test_data():
    user_data_list = [('Admin','admin123'),('Tom','welcome123')]
    return user_data_list

@allure.title("First testcase")
@allure.description("This is added for report purpose")
@allure.epic("Ness requirement")
@allure.story("Pytest - Allure reports")
@allure.tag("Smoke")
@allure.testcase("TC002","Test case - dummy")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('username,password',get_test_data())
def test_param(username,password):
    print(username)
    print(password)
    with allure.step("Step1"):
        allure.attach("Message", name="Log", attachment_type=allure.attachment_type.TEXT)
        with open("Stackroute.png", "rb") as f:
            allure.attach(f.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

