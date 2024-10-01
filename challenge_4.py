from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Function to scroll and count the total number of quotes
def count_quotes():
    # Path to the GeckoDriver (adjust if necessary)
    gecko_driver_path = r"geckodriver.exe"
    service = Service(gecko_driver_path)

    # Initialize the Firefox driver
    driver = webdriver.Firefox(service=service)

    try:
        # Step 1: Open the infinite scroll page
        driver.get('http://quotes.toscrape.com/scroll')

        # Initialize the number of quotes
        total_quotes = 0
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Step 2: Find all quote elements on the page
            quotes = driver.find_elements(By.CLASS_NAME, 'quote')
            total_quotes = len(quotes)

            # Step 3: Scroll down the page to load more quotes
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for the page to load
            time.sleep(2)  # Adjust if necessary

            # Step 4: Check if we've reached the end of the page
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # Print the total number of quotes
        print(f"\n\033[1;32mTotal number of quotes:\033[0m {total_quotes}\n")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    count_quotes()
