from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH, '//a[. = "JavaScript Alerts"]').click()

driver.find_element(By.XPATH, '//button[. = "Click for JS Alert"]').click()
print("Text for Click for JS Alert: ", driver.switch_to.alert.text)
driver.switch_to.alert.accept()

driver.find_element(By.XPATH, '//button[. = "Click for JS Confirm"]').click()
print("Text for Click for JS Confirm: ", driver.switch_to.alert.text)
driver.switch_to.alert.accept()

driver.find_element(By.XPATH, '//button[. = "Click for JS Prompt"]').click()
print("Text for Click for JS Prompt: ", driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("Aditya")
driver.switch_to.alert.accept()

driver.quit()
