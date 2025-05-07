# fill_form_multi.py
# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def open_and_fill_page(site_url, sample_data, click_submit):    
    # Initialize Chrome WebDriver with automatic driver management
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Open the form page
        driver.get(site_url)
    
        # Fill in the textboxes using their IDs from sample_data dictionary
        for control_id, value in sample_data.items():
            driver.find_element(By.ID, control_id).send_keys(value)
    
        # Optional, pause before clicking Submit or pressing Enter.
        time.sleep(2)  
        if click_submit:
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
        else:   
            # Get the last control ID from sample_data dictionary
            last_control_id = list(sample_data.keys())[-1]
            driver.find_element(By.ID, last_control_id).send_keys(Keys.RETURN)

        print("Form filled successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Keep the browser open for inspection
        print("Script completed; browser remains open.")
        input("Press Enter to exit the script and close the browser...")
        driver.quit()

def main():
    # Define site URL.
    site_url = "https://alansimpsonme.github.io/sampleform/form.html"  
    # Each key should be the id of the control to fill in the HTML form.
    sample_data = {
        "tbFirstName": "John",
        "tbLastName": "Doe",
        "tbUserName": "johndoe123",
        "tbCellPhone": "123-456-7890"
    }
    # Set to True to click the Submit button; otherwise False
    click_submit = True  # Set to True to click the Submit button; otherwise False
    
    # Open the page, fill the controls, and optionally click submit
    open_and_fill_page(site_url, sample_data, click_submit)

if __name__ == "__main__":
    main()