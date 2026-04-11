from selenium.webdriver import Chrome, ChromeOptions
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()
actions = ActionChains(driver)

driver.get("https://www.saucedemo.com/")

driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("asdfg")
driver.find_element(By.XPATH, '//input[@id="SHOPPER_PROFILE-button"]').click()

try:
    actual = driver.current_url
    excepted = "https://www.saucedemo.com/inventory.html"
    assert actual == excepted
    print("Test passed")

except AssertionError:
    # driver.save_screenshot("screenshot2.png")
    folder = os.path.join(os.getcwd(), 'SS_Folder')
    os.makedirs(folder, exist_ok=True)
    driver.save_screenshot(f'{folder}/screensht.png')

driver.quit()