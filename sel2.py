from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")

elem = driver.find_element_by_name("q")

elem.send_keys("go go anime")
elem.send_keys(Keys.RETURN)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "anime"))
)
element.click()

elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "keyword_search"))
)

elem.click()

elem.send_keys("steins gate")
elem.send_keys(Keys.RETURN)

elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Steins;Gate"))
)

elem.click()

elem = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "EP 25"))
)

elem.click()

elem = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btndownload"))
)

elem.click()

elem = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "Download openload"))
)

elem.click()



