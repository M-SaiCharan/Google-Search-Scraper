# Automated G search scraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def google_search_scraper(query, num_results=10):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
    
    for result in results:
        title = result.find_element(By.TAG_NAME, "h3").text
        link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
        desc = result.find_element(By.CSS_SELECTOR, 'span').text
        print(f"Title: {title}\nLink  : {link}\nDescription:\n\t{desc}")
        print("\n","-"*40,'\n')
    
    driver.quit()


google_search_scraper("python")