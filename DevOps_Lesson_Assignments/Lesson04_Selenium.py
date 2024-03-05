# import time
# from my_functions import checkpoint, highlight
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.firefox.options import Options
# import selenium

# print("Task 1. Write a script which will open the t2 .il sites in GC and in FF:")  # TESTED OK
# checkpoint("to open a link in Edge")
# print("a. Chrome: https://gmail.com :")
# link1a = "https://gmail.com"
# driver1a = webdriver.Edge()
# driver1a.get(link1a)
# driver1a.close()
# print()

# print("Task 2.")  # TESTED OK
# checkpoint("to create a variable with the website’s title (2a)")
# link21 = "https://dribbble.com/"
# driver2 = webdriver.Chrome()
# driver2.get(link21)
# print()
#
# checkpoint("to refresh website (Task 2b)")
# time.sleep(1)
# driver2.refresh()
# time.sleep(3)
# print()
#
# print("c. Get website name and compare it to the variable you")
# checkpoint("to check the windows still open (created in clause 1.)")
# link23 = driver2.current_url
# print(link2c)
# if link21 == link23:
#     print("they are the same")
# else:
#     print("they are NOT the same")
# driver2.close()

# print("# 3. Open a few browsers, locate any element")  # TESTED OK
# print("Does the element has the same locators in the other browser?")
# link3 = "https://google.com"
# driver31 = webdriver.Chrome()
# driver32 = webdriver.Firefox()
# driver31.get(link3)
# driver32.get(link3)
#
# element31 = driver31.find_element(By.NAME, "q")
# highlight(element31, 5)
# time.sleep(2)
#
# element32 = driver32.find_element(By.NAME, "q")
# highlight(element32, 5)
# time.sleep(2)

# print("4. Open Google Translate web page. Write anything in Hebrew in the text area")  # TESTED OK
# url4 = "https://translate.google.com"
# driver4 = webdriver.Chrome()
# driver4.get(url4)
# element4 = driver4.find_element(By.CSS_SELECTOR, ".er8xn")
# highlight(element4, 5)
# element4.send_keys("ברוך הבא")
# time.sleep(3)

# print("5. Open YouTube web page. Type a name of a song. Click on search.")  # TESTED OK
# url5 = "https://youtube.com"
# driver5 = webdriver.Chrome()
# driver5.get(url5)
# element5 = driver5.find_element(By.NAME, "search_query")
# element5.send_keys("Hafanana")
# element5.send_keys(Keys.RETURN)

# print("6. Open Chrome browser on Google Translate website:")  # TESTED OK
# url6 = "https://translate.google.com/"
# print("Let's find translation text field (the one you send keys to) with 3 different locators")
# print(" and print the WebElement you created.")
# driver6 = webdriver.Chrome()
# driver6.get(url6)
# print("selecting by the 'CSS-Selector'")
# element6 = driver6.find_element(By.CSS_SELECTOR, "textarea.er8xn")
# highlight(element6,3)
# time.sleep(2)
# print("selecting by the 'XPATH'")
# element66 = driver6.find_element(By.XPATH,
# "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
# highlight(element66,3)
# time.sleep(2)
# print("selecting by the 'Class'")
# element6666 = driver6.find_element(By.CLASS_NAME, "er8xn")
# highlight(element6666,3)

# print("Task 7.")  # TESTED OK
# checkpoint("to open Chrome browser on Facebook website")
# link7 = "https://www.facebook.com/"
# driver7 = webdriver.Chrome()
# driver7.get(link7)
# element71 = driver7.find_element(By.ID, "email")
# element71.send_keys("freelance_7@yahoo.com")
# element72 = driver7.find_element(By.ID, "pass")
# element72.send_keys("12345678")
# checkpoint("to login into Facebook")
# try:
#     element71.send_keys(Keys.RETURN)
#     element72.send_keys(Keys.RETURN)
#     time.sleep(5)
# except selenium.common.exceptions.StaleElementReferenceException:
#     print("Tested!")

# print("CHALLENGES")
# print("Task 8. Open Chrome browser on any webpage. Delete all cookies from browser.")
# print("Make sure all cookies are deleted by printing all cookies stored in the browser.")
# url8 = "https://google.com"
# driver8 = webdriver.Chrome()
# driver8.get(url8)
# cookies8 = driver8.get_cookies()
# print("Original cookies are: ")
# print(cookies8)
# list_cookies_names = []
# for list_cookies in cookies8:
#     cookies_name = list_cookies.get('name')
#     list_cookies_names.append(cookies_name)
# cookies8 = driver8.get_cookies()
# for cookie in list_cookies_names:
#     driver8.delete_cookie(cookie)
#     print(list_cookies_names)
# print("ONE_BY_ONE_DELETED cookies are: ")
# cookies8 = driver8.get_cookies()
# print(cookies8)


print("Task 9. Search")
# checkpoint("to open any browser on 'GitHub' website")
# link9 = "https://github.com/"
# driver9 = webdriver.Chrome()
# driver9.get(link9)
# driver9.maximize_window()
# element9 = driver9.find_element()
# element9.send_keys(Keys.RETURN)
# highlight(element9, 3)
# element9.send_keys("Selenium")
# element9.send_keys(Keys.RETURN)
# time.sleep(10)


# print("10. Find a way to disable all extensions in Chrome / Firefox / Internet Explorer.")
# print(" and run them without extensions.")
# https://www.browserstack.com/guide/test-chrome-extensions-in-selenium
