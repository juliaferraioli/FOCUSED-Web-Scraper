from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def get_dynamic_html(url):
    # Path to the Chrome WebDriver executable
    webdriver_path = '/path/to/chromedriver'

    # Create ChromeOptions object and set headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Create a Service object with the path to the WebDriver executable
    service = Service(webdriver_path)

    # Create a new instance of the Chrome driver with headless mode
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set the user agent string
    driver.execute_cdp_cmd(
        "Network.setUserAgentOverride",
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        },
    )

    # Navigate to the website
    driver.get(url)

    time.sleep(5)

    # Get the HTML content of the page
    html_text = driver.page_source

    # Close the browser
    driver.quit()
    return html_text
