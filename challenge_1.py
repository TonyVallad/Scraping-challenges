import requests
from bs4 import BeautifulSoup

# Base URL of the website
base_url = "http://books.toscrape.com/"

def get_soup(url):
    """ Helper function to send a request and return a BeautifulSoup object """
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Failed to retrieve content from {url}")
        return None

def get_categories():
    """ Scrapes the category URLs and names from the website """
    soup = get_soup(base_url)
    if soup:
        categories = {}
        side_categories = soup.find('div', class_='side_categories')
        category_links = side_categories.find_all('a')
        
        for link in category_links[1:]:  # Skipping the first link as it's "Books"
            category_name = link.text.strip()
            category_url = base_url + link['href']
            categories[category_name] = category_url
        
        return categories
    return {}

def scrape_books_in_category(category_url):
    """ Scrapes the total number of books and their prices in a single pass """
    soup = get_soup(category_url)
    if not soup:
        return 0, []

    # Get the total number of books from the first page
    total_books = int(soup.find('form', class_='form-horizontal').find('strong').text.strip())

    # Prepare to collect all book prices and count books across pages
    all_prices = []
    books_scraped = 0
    page_num = 1

    while books_scraped < total_books:
        # Adjust URL for pages after the first one
        if page_num == 1:
            page_url = category_url  # First page uses index.html
        else:
            page_url = f"{category_url.replace('index.html', '')}page-{page_num}.html"

        # Get the soup object for the current page
        soup = get_soup(page_url)
        if not soup:
            break  # If the page fails to load, break out of the loop

        # Scrape book prices on the current page
        articles = soup.find_all('article', class_='product_pod')
        for article in articles:
            price = article.find('p', class_='price_color').text.strip()
            price = float(price[1:])  # Convert to float after removing currency symbol
            all_prices.append(price)
        
        # Update the number of books scraped so far
        books_scraped += len(articles)
        page_num += 1  # Move to the next page

    return total_books, all_prices

def scrape_category_data():
    """ Scrapes the book count and average price for each category in a single pass """
    categories = get_categories()

    for category_name, category_url in categories.items():
        total_books, all_prices = scrape_books_in_category(category_url)

        # Calculate the average price
        if all_prices:
            total_price = sum(all_prices)
            average_price = total_price / len(all_prices)
        else:
            average_price = 0.0
        
        # Display results immediately after scraping each category
        print(f"Category: {category_name}")
        print(f"  Total Books: {total_books}")
        print(f"  Average Price: £{average_price:.2f}")

if __name__ == "__main__":
    # Scrape the category data and show the result for each category as soon as it's done
    scrape_category_data()
