from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'mishanja'
passwordStr = '198932'

browser = webdriver.Chrome()
browser.get('https://ts4.travian.com')

# fill in username and hit the next button

username = browser.find_element_by_name('name')
username.send_keys(usernameStr)

# wait for transition then continue to fill items

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))

password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('s1')
signInButton.click()
