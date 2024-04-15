import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

MY_MAIL = "julietsweet725@gmail.com"
MY_PASSWORD = "julie@2000"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
driver.maximize_window()

# adding delay because it takes time to actually load the elements onto the page
time.sleep(2)
# accepting the cookies
i_accept = driver.find_element(By.XPATH,
                               value='//*[@id="s686923397"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
i_accept.click()

time.sleep(2)
# clicking onto the login button
login_btn = driver.find_element(By.XPATH,
                                value='//*[@id="s686923397"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_btn.click()

time.sleep(2)
# click on login with Google
with_google_btn = driver.find_element(By.XPATH,
                                      value='/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div/div/div/div/iframe')
with_google_btn.click()

time.sleep(2)

base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
print(driver.title)

# switching to google window
driver.switch_to.window(google_login_window)

# typing in the email
email = driver.find_element(By.CSS_SELECTOR, 'input[type="email"].whsOnd.zHQkBf')
email.click()
email.clear()
email.send_keys(MY_MAIL, Keys.ENTER)

# wait for a few secs to let it load
time.sleep(2)

# typing in the password
password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"].whsOnd.zHQkBf')
password.click()
password.clear()
password.send_keys(MY_PASSWORD, Keys.ENTER)

time.sleep(2)

driver.switch_to.window(base_window)

time.sleep(2)

allow_cookies = driver.find_element(By.CSS_SELECTOR, value='.w1u9t036 .c9iqosj .lxn9zzn')
allow_cookies.click()

time.sleep(2)
turn_notifications = driver.find_element(By.CSS_SELECTOR, value='.w1u9t036 .c9iqosj .lxn9zzn')
turn_notifications.click()

time.sleep(2)

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1-second delay between likes.
    time.sleep(3)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/span')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(5)
