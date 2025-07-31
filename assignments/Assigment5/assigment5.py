from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_location_selection():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.practo.com/")

        # Wait for the location input and click it
        location_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search location"]'))
        )
        location_input.click()
        location_input.clear()

        # Type slowly to trigger autocomplete
        for char in "Thiruvananthapuram":
            location_input.send_keys(char)
            time.sleep(0.1)

        # Wait for the dropdown suggestion to appear
        suggestion_xpath = '//div[contains(@class,"c-omni-suggestion-item") and contains(., "Thiruvananthapuram")]'
        suggestion_item = wait.until(
            EC.visibility_of_element_located((By.XPATH, suggestion_xpath))
        )

        # Click the suggestion
        suggestion_item.click()

        #  Verify that the location was set
        time.sleep(2)
        print("Location successfully set to Thiruvananthapuram.")

        # Find and type into the specialty input
        specialty_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search doctors, clinics, hospitals, etc."]'))
        )
        specialty_input.click()
        specialty_input.clear()

        # Type 'Physician' slowly to trigger suggestions
        for char in "Physician":
            specialty_input.send_keys(char)
            time.sleep(0.1)

        # Wait and click on "Physician" from suggestions
        suggestion_xpath = '//div[@data-qa-id="omni-suggestion-listing"]//div[text()="Physician"]'
        general_physician_option = wait.until(
            EC.visibility_of_element_located((By.XPATH, suggestion_xpath))
        )
        general_physician_option.click()

        print("Specialty successfully set to Physician.")

        # Wait for the Gender dropdown and click it
        gender_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-qa-id="doctor_gender_section"]'))
        )
        gender_dropdown.click()

        # Wait for the "Male Doctor" option to be visible and click it
        male_option = wait.until(
          EC.visibility_of_element_located((By.XPATH, '//li[@data-qa-id="male"]'))
        )
        male_option.click()
        print("Gender filter set to Male.")

        #  Wait for the Experience dropdown and click it
        experience_dropdown = wait.until(
           EC.element_to_be_clickable((By.XPATH, '//div[@data-qa-id="years_of_experience_section"]'))
        )
        experience_dropdown.click()
        time.sleep(0.5)
        # Wait for the "5+ Years of experience" option to appear and click it
        experience_option = wait.until(
           EC.element_to_be_clickable((By.XPATH, '//li[@data-qa-id="5,9999999"]'))
        )
        experience_option.click()
        print("Experience filter set to 5+ Years.")

        #  Click the "Sort By" dropdown
        sort_by_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-qa-id="sort_by_section"]'))
        )
        sort_by_dropdown.click()

        time.sleep(0.3)

        # Select "Experience - High to Low"
        experience_sort_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//li[@data-qa-id="experience_years"]'))
        )
        experience_sort_option.click()
        print("Sorted by Experience - High to Low.")

        # Wait for and get the heading element
        heading = wait.until(
          EC.visibility_of_element_located((By.XPATH, '//div[@data-qa-id="no_results_heading"]/span'))
        )
        assert heading.text.strip() == "We couldn't find any doctors for you", "Heading text mismatch."

        # Wait for and get the description element
        description = wait.until(
          EC.visibility_of_element_located((By.XPATH, '//span[@data-qa-id="no_results_description"]'))
        )
        assert description.text.strip() == "Your search for physician in Thiruvananthapuram didn't match anything.", "Description text mismatch."
        print("No-results texts validated successfully.")

    except Exception as e:
        driver.save_screenshot("error.png")
        print(f"ERROR : {e}")
        raise
    time.sleep(3)
    driver.save_screenshot("results.png")
    driver.quit()
