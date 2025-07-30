import pytest
import webdriver_manager.chrome
from selenium import webdriver

# #scope = session, module, class , function
# @pytest.fixture(scope="session")
# def driver1():
#     driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager.install())
#     yield driver
#     driver.quit()


def pytest_report_teststatus(report):
    if report.when == "call":
        if report.outcome == "passed":
            print("Test passed:", report.nodeid)
        elif report.outcome == "failed":
            print("Test failed:", report.nodeid)
        elif report.outcome == "skipped":
            print("Test skipped:", report.nodeid)
        elif report.outcome == "xfailed":
            print("Test XFAIL:", report.nodeid)
        elif report.outcome == "xpassed":
            print("Test XPASS:", report.nodeid)
    # print(f"[{report.when.upper()}] {report.nodeid}: {report.outcome.upper()}")

# [SETUP] test_sample.py::test_example: PASSED
# [CALL] test_sample.py::test_example: PASSED
# [TEARDOWN] test_sample.py::test_example: PASSED