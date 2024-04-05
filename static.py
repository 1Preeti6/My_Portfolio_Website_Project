from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Start the WebDriver and open the HTML page
service = Service(executable_path='/usr/local/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://github.com/1Preeti6/My_Portfolio_Website_Project/blob/3e5ae679e927aedb75a9bd9b487c9b5d88659b10/PortfolioWebsite.html")  # Update this with the path to your HTML file

time.sleep(2)  # Adding a delay to see the result

# Assert some condition to verify the result
assert "My Portfolio Website" in driver.title

# Take a screenshot
timestamp = time.strftime("%Y%m%d-%H%M%S")
screenshot_file = f"screenshot_{timestamp}.png"
driver.save_screenshot(screenshot_file)

# Close the WebDriver
driver.close()
