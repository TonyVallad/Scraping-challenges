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

---

Feel free to copy this into your `README.md` file. If you need any adjustments or further explanations, let me know!