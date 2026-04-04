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

driver.get("https://in.pinterest.com/")
folder = os.path.join(os.getcwd(), 'SS_Folder')
os.makedirs(folder, exist_ok=True)
driver.save_screenshot(f'{folder}/screenshot.png')
ele = driver.find_element(By.XPATH, '//img[contains(@alt, "cherry-patterned sweater vest")]')
actions.move_to_element(ele).perform()
driver.save_screenshot(f'{folder}/screenshot_1.png')

driver.quit()

