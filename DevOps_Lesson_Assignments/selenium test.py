from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org/")

driver.captureNetworkTraffic()