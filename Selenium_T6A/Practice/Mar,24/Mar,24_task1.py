from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("http://x.com/")

driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@title="Sign in with Google Button"]'))
driver.find_element(By.XPATH, '//span[. = "Sign up with Google"]').click()
