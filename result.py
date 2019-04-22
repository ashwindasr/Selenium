'''
	Refresh a website for an update, every 1 min and send a mail to notify the user.
	
	Code is written for raspberry pi.
	
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display

def mail(subject,body):
	import email, smtplib, ssl

	from email import encoders
	from email.mime.base import MIMEBase
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	#subject = "An email with attachment from Python"
	#body = "This is an email with attachment sent from Python"
	sender_email = "***sender_email***"
	password = "***Password***"
	receiver_email = "***receiver_email***"

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject

	# Add body to email
	message.attach(MIMEText(body, "plain"))


	text = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, text)

display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Firefox()
driver.get("***website_link***")

mail("Script initialized","Driver initialized and running")
time.sleep(10)
a=False

while not a:
	try:
    		elem = WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "***unique_search_text_in_website")))
    		a=True
	except TimeoutException:
		time.sleep(60)
		driver.refresh()
if a:
	print("Success !")
	print(time.ctime())
	subject = "***mail_subject***"
	body = "***mail_body***"
	mail(subject,body)
	print("Mail sent")
	
