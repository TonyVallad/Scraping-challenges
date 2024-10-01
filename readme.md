# Web Scraping Challenges

This repository contains solutions to various web scraping challenges using Python. Each challenge utilizes different techniques and libraries to extract data from websites.

## Challenges

1. **What is the number of books and the average price found in each category on this website?**
   - [Website](https://books.toscrape.com/)
   - **Solution:** Scrape the total number of books and their average price from each category.

2. **Before answering the following questions, you will need to log into the website.**
   - [Login Page](http://quotes.toscrape.com/login)

3. **How many pages can be found on this website?**
   - [Website](https://quotes.toscrape.com/)

4. **How many quotes can be found at this URL?**
   - [Scroll Page](http://quotes.toscrape.com/scroll)

5. **What is the first quote on this link?**
   - [Quote Page](https://quotes.toscrape.com/js/page/10/)

6. **What is the fifth quote on this link?**
   - [Delayed Quote Page](http://quotes.toscrape.com/js-delayed/page/5/)

7. **What is the most repetitive tag on this page?**
   - [Tableful Quotes](http://quotes.toscrape.com/tableful/)

8. **What is the unique quote from Albert Einstein about music via this form?**
   - [Search Page](https://quotes.toscrape.com/search.aspx)

9. **How long will it take you to scrape all the content from this website?**
   - [Random Quote Page](http://quotes.toscrape.com/random)

## Challenge 1: Scraping Books and Average Prices

<img src="https://github.com/TonyVallad/Scraping-challenges/blob/main/challenge_1.png?raw=true" width="750"/>

In the first challenge, we scrape the [Books to Scrape](https://books.toscrape.com/) website to gather information about the number of books and their average prices in each category.

### Approach

1. **Requests and BeautifulSoup**: We used the `requests` library to fetch the HTML content of the website and `BeautifulSoup` to parse the HTML.
2. **Category Extraction**: We located the categories of books listed on the left side of the page within a `div` element.
3. **Pagination**: Each category might have multiple pages, so we iterated through each page to collect data about the books available in that category.
4. **Data Collection**: For each book, we extracted the price and maintained a count of the total number of books and their respective prices.
5. **Calculating Average Price**: After collecting all the prices for a category, we computed the average price and printed the results immediately.

### Example Code Snippet

Here’s a brief snippet demonstrating how we extracted the category names and prices:

```python
# Example of extracting categories
categories = get_categories()
for category_name, category_url in categories.items():
    total_books, all_prices = scrape_books_in_category(category_url)
    # Calculate average price and print results
    print(f"\033[1;32mCategory: {category_name}\033[0m")  # Category name in green
    print(f"  Total Books: {total_books}")
    print(f"  Average Price: £{average_price:.2f}")
```

This approach efficiently gathers and displays the necessary information without excessive requests to the server.

## Challenge 2: Logging into a Website

<img src="https://github.com/TonyVallad/Scraping-challenges/blob/main/challenge_2.png?raw=true" width="750"/>

**Objective:** Log into the website [Quotes to Scrape](http://quotes.toscrape.com/login) using Selenium.

**Solution:**
In this challenge, we used the **Selenium WebDriver** library to automate the login process. Here's the breakdown of the solution:

1. **Setup Selenium with GeckoDriver**: 
   - We initialized the **Firefox** WebDriver by specifying the path to `geckodriver.exe` using the `Service` class from Selenium.
   
2. **Navigating to the Login Page**:
   - Using Selenium's `get` method, we navigated to the login page (`http://quotes.toscrape.com/login`).

3. **Filling in the Login Form**:
   - We located the username and password input fields on the page using the `find_element` method with the `By.NAME` selector.
   - We then filled in the fields with the provided username and password using the `send_keys` method.

4. **Submitting the Form**:
   - The form was submitted by sending the `Keys.RETURN` action to the password field.

5. **Checking Login Success**:
   - We verified the login success by checking if the page source contained the word "Logout". If "Logout" was found, it confirmed that the login was successful; otherwise, the credentials were incorrect.

6. **Closing the WebDriver**:
   - After the process, the WebDriver was closed using the `quit` method to free up resources.

This solution provides a simple and efficient way to log into the site using valid credentials with Selenium WebDriver.

## Challenge 3: Determine the Total Number of Pages

<img src="https://github.com/TonyVallad/Scraping-challenges/blob/main/challenge_3.png?raw=true" width="750"/>

**Objective:** Find the total number of pages available on the [Quotes to Scrape](http://quotes.toscrape.com/) website.

**Solution:**
In this challenge, we used **BeautifulSoup** to scrape the website and determine the total number of pages. The website uses pagination to navigate between multiple pages of quotes, with a "Next" button indicating the presence of additional pages.

Here's how we approached the solution:

1. **Start at the First Page**:
   - We began by sending a GET request to the homepage (`http://quotes.toscrape.com/`) and parsed the HTML using BeautifulSoup.

2. **Identify and Follow the "Next" Button**:
   - We searched for the "Next" button in the page's pagination section. If it was found, we extracted the URL for the next page from the button's `href` attribute and updated our current URL.

3. **Count the Pages**:
   - Each time we found a "Next" button, we incremented the page counter. This process continued until the "Next" button was no longer present, indicating the last page.

4. **Final Output**:
   - Once the loop ended, we printed the total number of pages. For better readability in the terminal, the output was displayed in **green text** using ANSI escape codes.

This solution efficiently navigates through the website's paginated structure to find the total number of pages.

## Challenge 4: Determine the Total Number of Quotes on the Infinite Scroll Page

<img src="https://github.com/TonyVallad/Scraping-challenges/blob/main/challenge_4.png?raw=true" width="750"/>

**Objective:** Find the total number of quotes on the infinite scroll page of the [Quotes to Scrape](http://quotes.toscrape.com/scroll) website.

**Solution:**
The challenge here is that the website uses **infinite scrolling** to load new quotes dynamically as the user scrolls down. This means we can't just scrape all the content at once; instead, we need to continuously scroll down the page until all the quotes have been loaded.

To solve this, we used **Selenium** to simulate user interaction with the page, specifically scrolling down, and dynamically capturing all the quotes. Here’s the approach:

1. **Load the Infinite Scroll Page**:
   - We use **Selenium** to load the infinite scroll page of the website.

2. **Simulate Scrolling**:
   - Selenium executes a JavaScript command to scroll down the page repeatedly. After each scroll, we wait for the page to load more content before continuing.

3. **Capture and Count Quotes**:
   - After every scroll, we use Selenium to find and count all elements with the class `quote`, which represents each individual quote.

4. **Detect End of Scrolling**:
   - The script checks the height of the page (`document.body.scrollHeight`). When this height stops increasing after scrolling, we know we've reached the bottom, meaning no more quotes are being loaded.

5. **Output**:
   - The total number of quotes is printed to the terminal in **green text** for better readability.

This approach allows us to accurately scrape and count all quotes from an infinite scroll page.

## Challenge 5: Get the First Quote from Page 10 of a JavaScript-Generated Page

<img src="https://github.com/TonyVallad/Scraping-challenges/blob/main/challenge_5.png?raw=true" width="750"/>

**Objective:** Scrape the first quote from [page 10](http://quotes.toscrape.com/js/page/10/) of the JavaScript-rendered "Quotes to Scrape" website.

**Solution:**
In this challenge, the quotes are dynamically loaded through **JavaScript**, so using traditional scraping methods like `requests` and `BeautifulSoup` won't work as they only retrieve the static HTML. To solve this, we rely on **Selenium** to interact with the webpage, allowing it to fully render and load the quotes before scraping.

Here’s a summary of how we solved the problem:

1. **Using Selenium to Load the Page**:
   - Since the content is loaded dynamically via JavaScript, we used **Selenium** to open the page and wait for the content to load.

2. **Waiting for Quotes to Load**:
   - We introduced a slight delay (`time.sleep(2)`) to ensure that the quotes have enough time to fully render.

3. **Extracting the First Quote**:
   - Once the page is loaded, we located the first quote element using its class `quote`. From this element, we extracted the quote text and the author’s name.

4. **Displaying the Quote**:
   - We printed the first quote and its author in **cyan text** for readability in the terminal.

By using **Selenium**, we were able to interact with a JavaScript-heavy webpage and successfully scrape the first quote. This approach can be used for other pages that load content dynamically through JavaScript.

Here's the **Challenge 6** section for your `README.md` file:

## Challenge 6: Get the Fifth Quote from a Delayed JavaScript-Rendered Page

<img src="https://github.com/TonyVallad/Scraping-challenges/blob/main/challenge_6.png?raw=true" width="750"/>

**Objective:** Scrape the fifth quote from [page 5](http://quotes.toscrape.com/js-delayed/page/5/) of a JavaScript-rendered website where the quotes appear after a delay of approximately 10-12 seconds.

**Solution:**
In this challenge, the quotes on page 5 are loaded dynamically with a delay of around 10 to 12 seconds after the page initially loads. To handle this, we used **Selenium** to open the page, wait for the quotes to appear, and then extract the fifth quote.

**Approach:**
1. **Using Selenium to Load the Delayed Page**:
   - We used **Selenium** to open the URL since it can handle JavaScript and delays, unlike static web scrapers like `requests`.

2. **Handling the Delay**:
   - Since the quotes take around 10-12 seconds to appear, we introduced a wait time of 12 seconds (`time.sleep(12)`) to ensure the quotes are fully loaded before attempting to scrape them.

3. **Extracting the Fifth Quote**:
   - After waiting for the quotes to load, we used the `find_elements` method to collect all the quotes on the page.
   - We then checked if there are at least 5 quotes available and extracted the fifth one.

4. **Displaying the Quote**:
   - The fifth quote and its author were printed to the terminal in **cyan text** for improved readability.

**Code Summary**:
- **Selenium** was crucial in automating the browser and handling the delay caused by JavaScript rendering.
- The wait time was adjusted to 12 seconds to ensure the quotes had enough time to appear on the page.
- The quote and author information were scraped and displayed once the fifth quote was found.

