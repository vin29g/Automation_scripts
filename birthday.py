from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import getpass
import time

def page_loaded(driver):
	return driver.find_element_by_tag_name("body") != None

print("Enter Facebook Details:\n")
input_email_id = raw_input("Username/Email: ")
input_pwd = getpass.getpass()

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False

driver = webdriver.Firefox(capabilities=caps)

driver.get("https://www.facebook.com")
wait = ui.WebDriverWait(driver,10)
wait.until(page_loaded)

email = driver.find_element_by_id("email")
email.send_keys(input_email_id)
pwd = driver.find_element_by_id("pass")
pwd.send_keys(input_pwd)
pwd.send_keys(Keys.RETURN)

time.sleep(5)

driver.get("https://www.facebook.com/events/birthdays")
print("Loaded Birthday Page\n")

count = len(driver.find_elements_by_class_name("innerWrap"))
print(count)
for x in range(0,count):
	print("Start writing\n")
	text_box = driver.find_element_by_tag_name("textarea")
	text_box.send_keys("Happy Birthday!! \n")

	time.sleep(2)

driver.close()