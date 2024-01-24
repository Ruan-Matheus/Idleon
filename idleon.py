from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv("user")
password = os.getenv("password")


# What is this?
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)

# Acessing the site
driver.get(r"https://idleontoolbox.com/dashboard")


login_selector = '#__next > div.MuiBox-root.css-k008qs > header > div > div.MuiBox-root.css-zdpt2t > button'
email_name = 'email'
password_name = 'password'

# Wainting for the login buttom
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, login_selector))
)
login = driver.find_element(By.CSS_SELECTOR, login_selector)
login.click()


# Waiting for the login pop-up
WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.NAME, email_name))
)

# Signing
email_element = driver.find_element(By.NAME, email_name)
email_element.send_keys(user)
password_element = driver.find_element(By.NAME, password_name)
password_element.send_keys(password, Keys.ENTER)

WebDriverWait(driver, 6000).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "LOGOUT"))
)

driver.get("https://idleontoolbox.com/dashboard")
sleep(100000)
