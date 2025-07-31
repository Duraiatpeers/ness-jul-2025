import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_assigment4():
    base_url = 'https://weather.com'
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Accept cookies inside iframe with ID starting with "sp_message_iframe_"
    try:
        # Wait for the iframe to appear
        iframe = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[id^='sp_message_iframe_']"))
        )
        driver.switch_to.frame(iframe)

        # Wait for and click the "Accept all" button
        accept_all = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@title="Accept all" or contains(text(), "Accept all")]'))
        )
        accept_all.click()
        print("Clicked 'Accept all' button in iframe.")

        # Switch back to main content
        driver.switch_to.default_content()
        time.sleep(5)
    except Exception as e:
        driver.save_screenshot("fail_cookie_banner.png")
        print(f"ERROR: Could not handle cookie banner: {e}")
        raise

    # Search for Bengaluru
    # Click the first suggestion
    try:
        search_bar = wait.until(EC.element_to_be_clickable((By.ID, 'headerSearch_LocationSearch_input')))
        search_bar.clear()
        search_bar.send_keys('Bengaluru')
        time.sleep(5)

        try:
            first_suggestion = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"styles__item")]'))
            )
            print("Suggestion found:", first_suggestion.text)
            first_suggestion.click()
        except Exception as e:
            print(f"Suggestion not clickable, trying ENTER instead: {e}")
            search_bar.send_keys(Keys.ENTER)
            print("Pressed ENTER as fallback.")

        # Wait for some result to ensure navigation happened
        wait.until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(),"Bengaluru")]')))
        print("Search for Bengaluru completed.")

    except Exception as e:
        driver.save_screenshot("fail_search_bengaluru.png")
        print(f"ERROR: Search for Bengaluru failed: {e}")
        raise
    # Wait for 10-Day tab and click it
    try:
        xpath = '//a[.//span[text()="10 Day"]]'

        # First attempt
        ten_day_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", ten_day_link)
        ten_day_link.click()
        print("Clicked dynamic 10 Day link.")

    except StaleElementReferenceException:
        print("StaleElementReferenceException caught. Retrying...")
        try:
            ten_day_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", ten_day_link)
            ten_day_link.click()
            print("Clicked dynamic 10 Day link on retry.")
        except Exception as e:
            driver.save_screenshot("fail_10_day_retry.png")
            print(f"ERROR: Retry failed for '10 Day' link: {e}")
            raise
    except TimeoutException:
        driver.save_screenshot("fail_10_day.png")
        print(f"ERROR: Could not click '10 Day' link: {e}")
        raise
    except Exception as e:
        print(f"Could not click 10 Day link: {e}")
        raise

    #  Click the "More Forecasts" button
    try:
        more_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[contains(text(), "More")]]'))
        )

        actions = ActionChains(driver)
        actions.move_to_element(more_button).pause(1).click().perform()
        print("Hovered and clicked 'More Forecasts'.")

    except Exception as e:
        print(f"Failed to open More Forecasts: {e}")
        driver.save_screenshot("more_forecasts_failed_final_fix.png")
        raise

    # Click "Air Quality Forecast" link
    try:
        air_quality = wait.until(EC.element_to_be_clickable((
            By.XPATH, '//a[.//span[text()="Air Quality Forecast"]]'
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", air_quality)
        air_quality.click()
        print("Clicked Air Quality Forecast.")
    except Exception as e:
        print(f"Failed to click Air Quality Forecast: {e}")
        driver.save_screenshot("fail1_air_quality.png")
        raise
    # Click "Air Quality index" link
    try:
        air_quality_index_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, '//button[.//span[text()="Air Quality Index"]]')))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", air_quality_index_button)
        air_quality_index_button.click()
        print("Clicked 'Air Quality Index' button.")
    except Exception as e:
        print(f"Failed to click 'Air Quality Index' button: {e}")
        driver.save_screenshot("fail_click_air_quality_index.png")
        raise
    # Validate messages
    expected_body_text = (
        "Contains Copernicus Atmosphere Monitoring Service information 2025 "
        "and/or modified Copernicus Atmosphere Monitoring Service information 2025"
    )

    expected_footer_text = (
        "Neither the European Commission nor ECMWF is responsible for any use of this information"
    )

    try:
        # Wait for Air Quality Index container
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(@class,"AirQuality--popoverContent")]')
        ))

        # Validate body exact text
        body_element = wait.until(EC.presence_of_element_located((
            By.XPATH,
            '//div[contains(@class,"AirQuality--popoverText")]//p[1]'
        )))
        actual_body_text = body_element.text.strip()
        print("Body Text:", actual_body_text)
        assert actual_body_text == expected_body_text, "Body text does not match expected."

        # Validate footer exact text
        footer_element = wait.until(EC.presence_of_element_located((
            By.XPATH,
            '//div[contains(@class,"AirQuality--popoverText")]//p[2]'
        )))
        actual_footer_text = footer_element.text.strip()
        print("Footer Text:", actual_footer_text)
        assert actual_footer_text == expected_footer_text, "Footer text does not match expected."

    except AssertionError as ae:
        print(f"Assertion failed: {ae}")
        driver.save_screenshot("text_mismatch.png")
        raise

    except Exception as e:
        print(f"Unexpected error during popover validation: {e}")
        driver.save_screenshot("validation_exception.png")
        raise
    time.sleep(10)
    driver.close()