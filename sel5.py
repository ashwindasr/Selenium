from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(20)

elem = driver.find_element_by_xpath("//span[@title='Ashwin Titus']")

elem.click()

elem = driver.find_element_by_xpath("//div[@class='input']")

elem.click()


for x in range(100):
	elem.send_keys("Sorry... :(")
	elem.send_keys(Keys.RETURN)