from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)

driver.find_element(By.NAME, "email").send_keys("1234567890")
driver.find_element(By.NAME, "pass").send_keys("0123456789")
sleep(1)
driver.find_element(By.LINK_TEXT, "Log in").click()

sleep(2)
driver.quit()

