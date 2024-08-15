from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from googleFinancePage import googleFinancePage

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

pagedatUrl = "https://www.google.com/finance/"
testdata = ["NFLX", "MSFT", "TSLA"]


# Open the website and initialize the Page Object
driver.get(pagedatUrl)
finance_page = googleFinancePage(driver)

# Verify the title
expected_title = 'Google Finance - Stock Market Prices, Real-time Quotes & Business News'
assert driver.title == expected_title, f"Expected title '{expected_title}', but got '{driver.title}'"
print(f"Title check completed: \n {driver.title}")


# Retrieve and process stock symbols
symbolStock = finance_page.get_stock_symbols()
print(f"Retrieve all the stock Symbols listed under the section You may be interested in Info:\n {symbolStock}\n")
print(f"List of Stock symbol in (3) interested Info but missing in Testdata:\n {set(symbolStock) - set(testdata)} \n")
print(f"List of Stock symbol in Testdata but not in (3) listed info:\n {set(testdata) - set(symbolStock)}")

# Clean up
driver.quit()