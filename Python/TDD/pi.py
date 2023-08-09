import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract

# Set the path to your webdriver executable
webdriver_path = "./chromedriver"  # Update this with the actual path

# Initialize Chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)
chrome_service = ChromeService(executable_path=webdriver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the website
url = "https://www.google.com"  # Replace with the website you want to capture
driver.get(url)

# Wait for the page to load (adjust the time as needed)
time.sleep(5)

# Capture a screenshot of the page
screenshot_path = "screenshot.png"
driver.save_screenshot(screenshot_path)

# Close the browser
driver.quit()

# Use PyTesseract to extract text from the screenshot
image = Image.open(screenshot_path)
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
