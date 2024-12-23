from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from colorama import Fore, Style, init
import time

init(autoreset=True)

def google_search_scraper(query, num_results=10):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.google.com")

    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
    except TimeoutException:
        print(Fore.RED + "Search box not found. Exiting.")
        driver.quit()
        return

    time.sleep(2)

    results = []
    try:
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
        )
        for idx, result in enumerate(search_results):
            if idx >= num_results:
                break
            try:
                try:
                    title = result.find_element(By.TAG_NAME, "h3").text
                except NoSuchElementException:
                    title = "Title not available"

                try:
                    link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
                except NoSuchElementException:
                    link = "Link not available"

                try:
                    description = result.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
                except NoSuchElementException:
                    description = "Description not available"

                results.append({"title": title, "link": link, "description": description})
            except NoSuchElementException:
                continue
    except TimeoutException:
        print(Fore.RED + "Failed to load search results.")

    for idx, res in enumerate(results):
        print(Fore.YELLOW + f"Result {idx + 1}:")
        print(Fore.CYAN + Style.BRIGHT + f"Title       : {res['title']}")
        print(Fore.GREEN + Style.BRIGHT + f"Link        : {res['link']}")
        print(Fore.MAGENTA + f"Description : {res['description']}")
        print(Fore.RED + "\n" + "-" * 40 + "\n" + Style.RESET_ALL)

    driver.quit()

if __name__ == "__main__":
    query = input("Enter the topic to search : ")
    num = int(input("Enter the no. of results: "))
    print("\n")
    google_search_scraper(query, num)