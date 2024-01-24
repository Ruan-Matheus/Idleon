from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from time import sleep
import time
import os

load_dotenv()
user = os.getenv("user")
password = os.getenv("password")

login_selector = '#__next > div.MuiBox-root.css-k008qs > header > div > div.MuiBox-root.css-zdpt2t > button'
time_XPATH = '//*[@id="__next"]/div[1]/header/div/nav/div/span'
email_name = 'email'
password_name = 'password'
book_count_selector = '#__next > main > div > div > div.MuiStack-root.css-yd8sa2 > div.MuiStack-root.css-1uzyzyr > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiCard-root.css-1v84kb9 > div > h4'
closest_building_time_selector = '#__next > main > div > div > div.MuiStack-root.css-yd8sa2 > div.MuiStack-root.css-1uzyzyr > div.MuiGrid2-root.MuiGrid2-container.MuiGrid2-direction-xs-row.MuiGrid2-spacing-xs-1.css-1w4rhnr > div:nth-child(3) > div > div > div > span'
partial_text = "Printing is at maximum (storage) capacity for"

# What is this?
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(10) # seconds

# Acessing the site
driver.get(r"https://idleontoolbox.com/dashboard")

# Wainting for the login buttom
login = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, login_selector)))
login.click()

# Loging
email_element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, email_name)))
email_element.send_keys(user)
password_element = driver.find_element(By.NAME, password_name)
password_element.send_keys(password, Keys.ENTER)
    
# Wainting for longing sucessufully
WebDriverWait(driver, 6000).until(
    EC.presence_of_element_located((By.XPATH, time_XPATH))
)

while True: 
    # Refreshing the page after 1 or so
    driver.get("https://idleontoolbox.com/dashboard")

    book_count = driver.find_element(By.CSS_SELECTOR, book_count_selector)
    closest_building = driver.find_element(By.CSS_SELECTOR, closest_building_time_selector)
    printers = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, f"//*[contains(@aria-label, '{partial_text}')]")))

    print(f'\n\n\n{time.ctime(time.time())}')
    print(f'\n{book_count.text}')
    print(f"Closest building: " + closest_building.text)

    for printer in printers:
        sample = printer.get_attribute("aria-label")
        print(sample)
    sleep(60)

sleep(100000)