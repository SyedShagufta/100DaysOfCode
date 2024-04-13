from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie = driver.find_element(By.ID, value="cookie")

start_time = time.time()
while time.time() - start_time < 300:  # Run for 5 minutes
    timeout = time.time() + 5
    while time.time() < timeout:
        cookie.click()

    add_ons_list = driver.find_elements(By.CSS_SELECTOR, "#store div")

    # Find the last non-grayed element
    last_non_grayed = None
    for add_on in reversed(add_ons_list):
        if "grayed" not in add_on.get_attribute("class"):
            last_non_grayed = add_on
            break

    # Click on the last non-grayed element if found
    if last_non_grayed:
        last_non_grayed.click()

# After 5 minutes, print the result for the element with ID "cps"
cps_element = driver.find_element(By.ID, "cps")
print("CPS:", cps_element.text)

# Close the browser
driver.quit()
