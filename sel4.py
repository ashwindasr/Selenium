from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://ww1.gogoanime.io/")
time.sleep(10)
a=False

while not a:
	try:
    		elem = WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Rokudenashi")))
    		a=True
	except TimeoutException:
		time.sleep(60)
    		driver.refresh()
if a:
	print("Its Released!!")
	print(time.ctime())
