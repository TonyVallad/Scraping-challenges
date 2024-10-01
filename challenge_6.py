from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Function to get the fifth quote from the delayed page 5
def get_fifth_quote_from_page_5():
    # Path to the GeckoDriver (adjust if necessary)
    gecko_driver_path = r"geckodriver.exe"
    service = Service(gecko_driver_path)

    # Initialize the Firefox driver
    driver = webdriver.Firefox(service=service)

    try:
        # Step 1: Open the page 5 with delayed quotes
        driver.get('http://quotes.toscrape.com/js-delayed/page/5/')

        # Wait for the quotes to load (they take approximately 10 seconds to load)
        time.sleep(12)

        # Step 2: Find all quote elements
        quotes = driver.find_elements(By.CLASS_NAME, 'quote')

        # Step 3: Check if there are at least 5 quotes
        if len(quotes) >= 5:
            # Extract the fifth quote's text and author
            fifth_quote = quotes[4]
            quote_text = fifth_quote.find_element(By.CLASS_NAME, 'text').text
            quote_author = fifth_quote.find_element(By.CLASS_NAME, 'author').text

            # Print the fifth quote and its author
            print(f'\n\033[1;36mFifth Quote on Page 5:\033[0m "{quote_text}" - {quote_author}\n')
        else:
            print("Less than 5 quotes found on the page.")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    get_fifth_quote_from_page_5()
