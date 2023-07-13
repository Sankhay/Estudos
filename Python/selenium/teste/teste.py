from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Open the link using Selenium
driver = webdriver.Chrome()
driver.get("https://www.google.com")  # Replace with your desired link
time.sleep(10)
    # Get the HTML content of the page
    #html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
#soup = BeautifulSoup(html_content, "html.parser")

# Find the link you want to open within the HTML
#link_element = soup.find("a", href="your_link_here")  # Replace with the appropriate selector

# Extract the href attribute from the link element
#link_url = link_element["href"]

# Open the link using Selenium
driver.get('https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25')

    # Continue with further actions on the loaded page

# The Selenium driver will be automatically closed at the end of the 'with' block
