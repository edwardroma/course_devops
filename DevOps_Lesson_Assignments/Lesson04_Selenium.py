from my_functions import checkpoint
from selenium import webdriver
from selenium.webdriver.common.by import By


print("Task 1. Write a script which will open the t2 .il sites in GC and in FF:")
checkpoint("to open a link in GC")
print("a. Chrome: http://www.walla.co.il :")
driver1 = webdriver.Chrome()
driver1.maximize_window()
driver1.get("http://www.walla.co.il")


checkpoint("to open a link in FF")
print("b. FireFox – http://www.google.com : ")
driver2 = webdriver.Firefox()
driver2.get("http://www.google.com")
driver2.find_element(By.NAME, "q")


print(" Task 2. In a browser: create variable, refresh website")
checkpoint("to create a variable with the website’s title")
website1 = "https://www.amason.com"


# pause("to refresh website")
# driver.get("http://www.amazon.com")
# driver.refresh()

# c. Get website name and compare it to the variable you
# created in clause 1.
# website2 = driver.current_url
# print(website2)
# if website1 == website2:
#     print("they are the same")
# else:
#     print("they are NOT the same")

# 3. Open a few browsers, locate any element, does the
# element has the same locators in the other browser?
#
# 4. Create a test with the following:
#  Open Google Translate web page
#  Write anything in Hebrew in the text area
#
# 5.
#  Open YouTube web page
#  Type a name of a song
#  Click on search.
#
# 6.
#  Open Chrome browser on Google Translate website:
# https://translate.google.com/
#  Find translation text field (the one you send keys to)
# with 3 different locators and print the WebElement
# you created.
#
# 7.
#  Open Chrome browser on Facebook website
# https://www.facebook.com/
#  Login into Facebook (No need to send me credentials).
#
# CHALLENGES:
# 8.
#  Open Chrome browser on any webpage.
#  Delete all cookies from browser.
#  Make sure all cookies are deleted by printing all cookies
# stored in the browser.
#
# 9.
#  Open any browser on "GitHub" website.
#  https://github.com/
#  Enter “Selenium” keyword in search textfield
#  Press Enter to search (through code - of course).
#
# 10.
#  Find a way to disable all extensions in
# o Chrome
# o Firefox
# o Internet Explorer.
#  Run browsers without extensions.
