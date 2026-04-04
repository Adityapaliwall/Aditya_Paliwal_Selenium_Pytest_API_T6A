from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.select import Select
import os
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.lenskart.com/")
driver.find_element(By.XPATH, '//a[@id="lrd1"]').click()
actual = "https://www.lenskart.com/eyeglasses.html"
expected = driver.current_url

assert actual == expected

driver.find_element(By.XPATH, '//select[@id="sortByDropdown"]').click()
driver.find_element(By.XPATH, '//option[. = "Most Viewed"]').click()
driver.find_element(By.XPATH, '//select[@id="sortByDropdown"]').click()

folder = os.path.join(os.getcwd(), 'SS_Folder')
os.makedirs(folder, exist_ok=True)
driver.save_screenshot(f'{folder}/Screenshot_2.png')

driver.quit()

