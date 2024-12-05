from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Set up the WebDriver (e.g., ChromeDriver).
driver = webdriver.Chrome()  # You need to have ChromeDriver installed and in PATH.

# Step 2: Open Google's search page.
driver.get("https://www.google.com")

# Step 3: Find the search bar and input a query.
search_box = driver.find_element(By.NAME, "q")  # Google’s search bar has the name "q".
search_box.send_keys("Python programming")  # Enter the search query.
search_box.send_keys(Keys.RETURN)  # Press Enter to search.

# Step 4: Wait for results to load.
time.sleep(3)  # Wait to ensure the results are fully loaded (you can optimize this).

# Step 5: Scrape the search result titles and links.
results = driver.find_elements(By.CSS_SELECTOR, "div.g")  # Each search result is in a div with class "g".

for result in results:
    title = result.find_element(By.TAG_NAME, "h3").text  # Get the title text.
    link = result.find_element(By.TAG_NAME, "a").get_attribute("href")  # Get the link URL.
    print(f"Title: {title}")
    print(f"Link: {link}")
    print("-" * 40)

# Step 6: Close the browser.
driver.quit()
