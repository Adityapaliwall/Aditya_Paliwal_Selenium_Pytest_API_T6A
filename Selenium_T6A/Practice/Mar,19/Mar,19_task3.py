from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()

driver.find_element(By.XPATH, '//a[. = "Register"]').click()

driver.find_element(By.XPATH, '//input[@id="gender-male"]').click()
driver.find_element(By.XPATH, '//input[@id="FirstName"]').send_keys("John")
driver.find_element(By.XPATH, '//input[@id="LastName"]').send_keys("Doe")
driver.find_element(By.XPATH, '//input[@id="Email"]').send_keys("asd@asd.com")
driver.find_element(By.XPATH, '//input[@id="Password"]').send_keys("as12@12")
driver.find_element(By.XPATH, '//input[@id="ConfirmPassword"]').send_keys("as12@12")
driver.find_element(By.XPATH, '//input[@id="register-button"]').click()