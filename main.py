from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import sys

browser = webdriver.Chrome()

USERNAME = ""
PASSWORD = ""

try:
    browser.get('https://student.etf.bg.ac.rs/security/login.jsf')
    browser.maximize_window()

    username = sys.argv[1]
    password = sys.argv[2]
    if USERNAME != "":
        username = USERNAME
    if PASSWORD != "":
        password = PASSWORD

    browser.find_element(By.NAME, "j_username").send_keys(username)
    browser.find_element(By.NAME, "j_password").send_keys(password)
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
        browser.find_element(By.ID, "main:finish").click()

        time.sleep(1)
        browser.find_element(By.ID, "main:save").click()
    except:
        break
browser.quit()
print("Gotovo")