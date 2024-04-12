from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("sofia", Keys.ENTER)
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("syed", Keys.ENTER)
email = driver.find_element(By.NAME, "email")
email.send_keys("sofia@gmail.com", Keys.ENTER)

