from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.selenium.dev/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Downloads").click()
sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT, "English").click()
sleep(1)

driver.find_element(By.LINK_TEXT, "Register now!").click()
sleep(1)
print(driver.title)

driver.quit()

