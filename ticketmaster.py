from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


CHROMEDRIVER_PATH = "/Users/path/Downloads/chromedriver-mac-arm64/chromedriver"  
TICKETMASTER_URL = "https://www.ticketmaster.de/event/541899?referrer=https://www.ticketmaster.de/event/billie-eilish-hit-me-hard-and-soft-the-tour-tickets/541899&queueittoken=e_abgermany5418995g~ts_1746788246~ce_true~q_b5e606c2-8c47-4db3-af1a-67dc071165a4~rt_queue~ti_f8922745-1a8c-493b-ab5e-bf08429b2892~h_8247e16e5ce05fcfca5190d4f48b71c18fadbbd84d61e7d52023ea0a9a20d81a" 

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(TICKETMASTER_URL)
time.sleep(3)

while True:
    try:
        tickets_button = driver.find_element("xpath", "//span[text()='Tickets']")
        tickets_button.click()
        print("🎟️ Clicked 'Tickets' button")
        time.sleep(4)
    except:
        pass

    try:
        retry_button = driver.find_element("xpath", "//span[text()='Erneut suchen']")
        retry_button.click()
        print("🔁 Clicked 'Erneut versuchen' button")
        time.sleep(4)
    except:
        pass

    time.sleep(1)
