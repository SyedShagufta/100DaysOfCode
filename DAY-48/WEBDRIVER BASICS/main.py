import time

from selenium.webdriver.firefox.options import Options

from selenium import webdriver

# Keep browser open even after the program finishes
# create a firefox profile
profile = webdriver.FirefoxProfile()

# Set preferences to prevent the browser from closing immediately
profile.set_preference("browser.tabs.remote.autostart", False)
profile.set_preference("browser.tabs.remote.autostart.1", False)
profile.set_preference("browser.tabs.remote.autostart.2", False)

# Instantiate FirefoxOptions and pass the custom profile
options = Options()
options.profile = profile

# Instantiate the Firefox WebDriver with the custom profile
driver = webdriver.Firefox(options=options)

# driver = webdriver.Firefox()
driver.get("https://www.amazon.com")
time.sleep(100)

driver.quit()
