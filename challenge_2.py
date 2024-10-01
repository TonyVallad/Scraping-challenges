from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service  # Import Service for Firefox
import time
import os

# Function to log into the site
def login_to_quotes(username, password):
    # Set the path to the GeckoDriver
    gecko_driver_path =  r"geckodriver.exe"  # Adjust this if necessary

    # Initialize the Firefox driver using the Service object
    service = Service(gecko_driver_path)
    driver = webdriver.Firefox(service=service)

    try:
        # Step 1: Open the login page
        driver.get("http://quotes.toscrape.com/login")

        # Step 2: Find the username and password fields and log in
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Wait for a few seconds to ensure the page loads
        time.sleep(2)  # Adjust this time based on your internet speed

        # Step 3: Check if login was successful
        if "Logout" in driver.page_source:
            print("Login successful!")
        else:
            print("Login failed. Please check your credentials.")

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    # Replace 'your_username' and 'your_password' with valid credentials
    login_to_quotes('admin', '1234')
