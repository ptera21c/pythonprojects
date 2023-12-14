from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up the web driver
driver = webdriver.Chrome()  # You can replace Chrome with the browser of your choice
driver.get("https://ach.alayacare.com/#/scheduling/staff/default/view")

# Perform the login
email = driver.find_element("name", "email")  # Change "username" to the actual name of the username field
password = driver.find_element("name", "password")  # Change "password" to the actual name of the password field

email.send_keys(email)
password.send_keys(password)
password.send_keys(Keys.RETURN)

time.sleep(10)
# Wait for the next page to load if necessary
# Add necessary delay here if the next page takes time to load after login

# Now that you are logged in, you can scrape the data
soup = BeautifulSoup(driver.page_source, "html.parser")
# Use BeautifulSoup to find the elements you need
# Use the appropriate BeautifulSoup methods here

parent_element = driver.find_element(By.CSS_SELECTOR, '#calendar > div.fc-toolbar > div.fc-left > div > select.calendar.select')  # Replace "parent_class_name" with the actual class name of the parent element
parent_element.click()

time.sleep(10)
# Now you can navigate to the select element from the parent element
option =driver.find_element(By.CSS_SELECTOR, '#calendar > div.fc-toolbar > div.fc-left > div > select.calendar.select > option:nth-child(4)')
time.sleep(10)
option.click()

# Select an option by its value
#select_element.select_by_value("month")  # Replace "option_value" with the actual value you want to select


time.sleep(10)  # Change the delay as needed



address = driver.find_elements(By.CLASS_NAME, 'fc-title')

#finishedjob_elements = results.find_all("div", class_="fc-day-grid-event fc-h-event fc-event fc-start fc-end approved completed")
#travel_elements = results.find_all("div", class_="patient-address")

print(address)

#popover208064 > div.popover-content > div > div.patient-address<div class="patient-address">

# Close the browser after scraping
#//*[@id="calendar"]/div[1]/div[1]/div/select[2]/option[4]<option value="month">Month</option>/html/body/div[1]/div[4]/div[2]/div/div/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/select[2]/option[4]
#calendar > div.fc-toolbar > div.fc-left > div > select.calendar.select > option:nth-child(4)
