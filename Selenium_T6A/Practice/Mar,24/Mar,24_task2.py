from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://www.zomato.com/login")
# driver.find_element(By.XPATH, '//i[contains(@class,"sc-rbbb40-1 cLEXmC sc-re4bd0-1 bKymEa")]').click()

sleep(3)
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="auth-SHOPPER_PROFILE-ui"]'))
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="Sign in with Google Button"]'))
driver.find_element(By.XPATH, '//span[. = "Sign in with Google"]').click()
