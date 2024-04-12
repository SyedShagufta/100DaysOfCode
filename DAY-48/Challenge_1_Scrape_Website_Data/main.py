from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

date = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last > div > ul > li > time")
dates = ['2024-'+d.text for d in date]
title = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last > div > ul > li > a")
titles = [t.text for t in title]

print(dates)
print(titles)

events = {}
for e in range(0, len(dates)):
    events[e] = {
        "time": dates[e],
        "name": titles[e]
    }

print(events)
driver.quit()
