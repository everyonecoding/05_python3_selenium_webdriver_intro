from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



chromedriver = '/usr/local/bin/chromedriver_100'

driver = webdriver.Chrome(chromedriver)
driver.get("https://google.com")

element_q = driver.find_element_by_name("q")
element_q.send_keys("人人有CODE DUP")
element_q.submit()


#2. XPath
xpath = '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/a'
WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

#3. Google Sign in
signin_button = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a'
email_input = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
password_input = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
next_button = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'

WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, signin_button))).click()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, email_input))).send_keys("----Your email here----")
driver.find_element_by_xpath(next_button).click()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, password_input))).send_keys("----Your Login Password----")
driver.find_element_by_xpath(next_button).click()

#Subscribe
subscribe_button = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/ytd-subscribe-button-renderer/tp-yt-paper-button'
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, subscribe_button))).click()

