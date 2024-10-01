import requests
from bs4 import BeautifulSoup

# Function to extract the total number of pages from the website
def get_total_pages():
    # Base URL of the website
    base_url = 'http://quotes.toscrape.com'
    current_url = base_url

    # Variable to store the current page number
    total_pages = 1

    while True:
        # Send a GET request to fetch the current page's HTML content
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the "Next" button in the pagination section
        next_button = soup.find('li', class_='next')

        if next_button:
            # Extract the href of the "Next" button
            next_page_url = next_button.find('a')['href']
            current_url = base_url + next_page_url

            # Extract the page number from the URL
            total_pages += 1
        else:
            # No "Next" button means we've reached the last page
            break

    # Added line for better readability
    print()

    # Print the total number of pages
    print(f'\033[1;32mTotal number of pages:\033[0m {total_pages}') # With green text for better readability

    # Added line for better readability
    print()

if __name__ == "__main__":
    get_total_pages()
