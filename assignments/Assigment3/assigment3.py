import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
@pytest.fixture()
def driver():
    service = Service(executable_path="C:\\WebDrivers\\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("https://www.ust.com/en/careers")
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()

def test_assignment3(driver):
    print('Main window URL:', driver.current_url)
    print('Main window handle:', driver.current_window_handle)

    # main_window = driver.current_window_handle
    # driver.find_element(By.LINK_TEXT, 'Careers').click()
    WebDriverWait(driver, 10).until( ec.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
    try:
        cookie_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        if cookie_button.is_displayed():
            cookie_button.click()
            time.sleep(2)
    except Exception as e:
        print("Cookie consent not found or already handled:", e)

   # Click the icon/button that opens a new window
    driver.find_element(By.XPATH,'//div[contains(@class, "ust-homepage-hero_icon-wrapper")]').click()
    time.sleep(10)
    all_windows = driver.window_handles
    assert len(all_windows) > 1, "No new window opened"
    child_window = all_windows[1]
    driver.switch_to.window(child_window)
    print('Child window URL:', driver.current_url)
    print('Child window handle:', driver.current_window_handle)
    WebDriverWait(driver, 40).until(ec.element_to_be_clickable((By.XPATH, '//button[contains(@class, "btn-primary-search")]')))
    driver.find_element(By.XPATH, '//input[@placeholder="Type a job name, role or skill"]').send_keys('test automation')
    driver.find_element(By.XPATH, '//span[@title="Location"]//i[@class="icon-glyph-35 float-right"]').click()
    driver.find_element(By.XPATH, '//input[@value="Trivandrum"]').click()
    driver.find_element(By.XPATH, '//span[contains(@class, "experience-btn")]').click()
    driver.find_element(By.XPATH, '//input[@value="7"]').click()
    driver.find_element(By.XPATH, '//button[contains(@class, "btn-primary-search")]').click()
    time.sleep(10)
    results_number = driver.find_element(By.XPATH, '//div[contains(@class, "row result")]').text
    assert results_number == "153 job(s) found"
