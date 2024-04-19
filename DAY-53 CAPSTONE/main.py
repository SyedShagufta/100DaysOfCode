import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
                            "Accept-Language": "en-US,en;q=0.5",
                        }
                        )
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

# list of links
links = [link["href"] for link in soup.findAll(class_="property-card-link")]

# list of addresses
addresses = [address.getText().replace("|", " ").strip() for address in soup.findAll(name="address")]

# list of prices
prices = [price.getText().replace("/mo", "").split("+")[0] for price in
          soup.findAll(name="span", class_="PropertyCardWrapper__StyledPriceLine")]


driver = webdriver.Chrome()

for i in range(len(links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScEeYu4yOAxl9am0N_70x-bcU8v4gfMKEVWxnAHNKY64CBk0w/viewform")
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    lst_inp = driver.find_elements(By.CSS_SELECTOR, value=".whsOnd.zHQkBf")
    submit_btn = driver.find_element(By.CSS_SELECTOR, value=".Y5sE8d > span:nth-child(3) > span:nth-child(1)")
    lst_inp[0].click()
    lst_inp[0].send_keys(addresses[i])
    lst_inp[1].click()
    lst_inp[1].send_keys(prices[i])
    lst_inp[2].click()
    lst_inp[2].send_keys(links[i])
    submit_btn.click()

