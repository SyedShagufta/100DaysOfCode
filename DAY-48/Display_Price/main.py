# class name - _30jeq3 _16Jk6d
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.flipkart.com/samsung-galaxy-book3-intel-core-i5-13th-gen-1335u-16-gb-512-gb-ssd-windows-11-home-thin-light-laptop/p/itm9c25e72104066?pid=COMGN5FVZXFK26KS&lid=LSTCOMGN5FVZXFK26KSM6BP7L&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_3&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&fm=organic&iid=bb3af0ec-21b9-400e-91b9-baadcc3d32c7.COMGN5FVZXFK26KS.SEARCH&ppt=hp&ppn=homepage&ssid=3ziely5uym49i4g01712845301494")

title = driver.find_element(By.CLASS_NAME, value="B_NuCI").text
price = driver.find_element(By.CSS_SELECTOR, value="._30jeq3._16Jk6d").text

print(f"The price of the {title} is {price}")

driver.quit()
