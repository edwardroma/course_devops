from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# link: str = "https://www.google.com"
# checkpoint(f"to open {link}")
# print("Chrome goes to Chrome: ")
#
# driver1 = webdriver.Chrome()
# driver1.maximize_window()
# driver1.get(link)
#
# element1 = driver1.find_element(By.NAME, "q")
# element1.send_keys("LinkedIn Login")

driver = webdriver.Firefox()
driver.get("https://www.google.com/")
element = driver.find_element(By.NAME, "q")

# send keys
element.send_keys("Arrays")
element.send_keys(Keys.RETURN)
