from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Function to get the first quote from page 10
def get_first_quote_from_page_10():
    # Path to the GeckoDriver (adjust if necessary)
    gecko_driver_path = r"geckodriver.exe"
    service = Service(gecko_driver_path)

    # Initialize the Firefox driver
    driver = webdriver.Firefox(service=service)

    try:
        # Step 1: Open the page 10 of quotes
        driver.get('http://quotes.toscrape.com/js/page/10/')

        # Wait for the quotes to load
        time.sleep(2)  # Adjust based on your internet speed

        # Step 2: Find the first quote element
        first_quote = driver.find_element(By.CLASS_NAME, 'quote')

        # Extract the text of the first quote and the author
        quote_text = first_quote.find_element(By.CLASS_NAME, 'text').text
        quote_author = first_quote.find_element(By.CLASS_NAME, 'author').text

        # Step 3: Print the first quote and its author
        print(f'\n\033[1;36mFirst Quote on Page 10:\033[0m "{quote_text}" - {quote_author}\n')

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    get_first_quote_from_page_10()
