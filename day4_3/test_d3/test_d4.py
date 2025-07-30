import allure
import pytest


def get_test_data():
    user_data_list = [('Admin','admin123'),('Tom','welcome123')]
    return user_data_list

@allure.title("Second testcase")
@allure.description("This is added for report purpose")
@allure.epic("Ness requirement")
@allure.story("Pytest - Allure reports")
@allure.tag("Smoke")
@allure.testcase("TC002","Test case - dummy")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('username,password',get_test_data())
def test_param1(username,password):
    print(username)
    print(password)
    assert False


@allure.title("Third testcase")
@allure.description("This is added for report purpose")
@allure.epic("Ness requirement")
@allure.story("Pytest - Allure reports")
@allure.tag("Smoke")
@allure.testcase("TC002","Test case - dummy")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail
def test_param2():
    assert False


@allure.title("Fourth testcase")
@allure.description("This is added for report purpose")
@allure.epic("Ness requirement")
@allure.story("Pytest - Allure reports")
@allure.tag("Smoke")
@allure.testcase("TC002","Test case - dummy")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.skip
def test_param3():
    assert False


@allure.title("Fifth testcase")
@allure.description("This is added for report purpose")
@allure.epic("Ness requirement")
@allure.story("Pytest - Allure reports")
@allure.tag("Smoke")
@allure.testcase("TC003","Test case - dummy")
@allure.severity(allure.severity_level.MINOR)
def test_param4():
    assert False
