from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import sys

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get('https://student.etf.bg.ac.rs/security/login.jsf')
    browser.maximize_window()

    browser.find_element(By.NAME, "j_username").send_keys(sys.argv[1])
    browser.find_element(By.NAME, "j_password").send_keys(sys.argv[2])
    browser.find_element(By.NAME, "login").click()

    time.sleep(.2)
    browser.find_element(By.ID, "menu_nav1_txt18").click()
except:
    print("Los username")
    browser.close()

while (True):
    try:
        time.sleep(.2)
        browser.find_element(By.CLASS_NAME, "okCancelButton").click()

        time.sleep(.2)
        try:
            select = Select(browser.find_element(By.ID, "main:ddlNastavnik"))
            select.select_by_index(random.randint(1, 2))
        except:
            print("Nema profesora")

        radio_buttons = browser.find_elements(By.CSS_SELECTOR, "input[type='radio']")
        random.shuffle(radio_buttons)
        for button in radio_buttons:
            button.click()
        browser.find_element(By.ID, "main:grupaPitanja:0:pitanje:5:uirepeat:0:tekstKorisnika2").send_keys("Izmedju " + str(random.randint(1, 5)) + " i " + str(random.randint(6, 15)))
        browser.find_element(By.ID, "main:finish").click()

        time.sleep(.2)
        browser.find_element(By.ID, "main:save").click()
    except:
        break
browser.close()
print("Gotovo")