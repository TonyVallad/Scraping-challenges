from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Function to get the most repetitive quote-related tag on the page using Selenium
def get_most_repetitive_quote_tag():
    # Path to the GeckoDriver (adjust if necessary)
    gecko_driver_path = r"geckodriver.exe"
    service = Service(gecko_driver_path)

    # Initialize the Firefox driver
    driver = webdriver.Firefox(service=service)

    try:
        # Step 1: Open the page with the quote-related tags
        driver.get('http://quotes.toscrape.com/tableful/')

        # Step 2: Allow time for the page to load
        time.sleep(2)

        # Step 3: Locate the <td> section containing the tags and find all <a> tags
        tag_elements = driver.find_elements(By.CSS_SELECTOR, 'td a')

        # Step 4: Create a dictionary to count occurrences of each tag
        tag_counts = {}

        # Step 5: Extract and count each tag's text
        for tag_element in tag_elements:
            tag_text = tag_element.text.strip()  # Clean up whitespace
            if tag_text in tag_counts:
                tag_counts[tag_text] += 1
            else:
                tag_counts[tag_text] = 1

        # Step 6: Find the most common tag and its count
        if tag_counts:
            most_common_tag = max(tag_counts, key=tag_counts.get)
            count = tag_counts[most_common_tag]

            # Print the most repetitive tag and its count
            print(f'\n\033[1;35mMost Repetitive Quote Tag:\033[0m "{most_common_tag}" appears {count} times\n')
        else:
            print("No tags found on the page.")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    get_most_repetitive_quote_tag()
