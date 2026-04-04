from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.bmrc.co.in/")
driver.implicitly_wait(10)

sleep(2)
driver.find_element(By.XPATH, '//span[.="English"]').click()

dropdown1 = driver.find_element(By.XPATH, '//select[@class="form-control select fare-selects"]')
option1 = Select(dropdown1)
option1.select_by_visible_text("Benngiganahalli")

dropdown2 = driver.find_element(By.XPATH, '(//select[@class="form-control select fare-selects"])[2]')
option2 = Select(dropdown2)

option2.select_by_visible_text("Kengeri")

driver.find_element(By.XPATH, '//button[@class="app-btn-box"]').click()

driver.quit()