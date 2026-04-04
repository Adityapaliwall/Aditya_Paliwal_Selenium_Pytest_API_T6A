"""
Assertion:
        -> using Assert we are validating that outcome is same as favourable outcome or not
        -> Assertion is used to verify expected vs actual result in test cases.
        -> If condition fails → test case fails immediately.
"""
import os

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

########################################################################################################################
# driver.get("https://www.google.com/")
#
# expected = 'Google'
# actual = driver.title
#
# assert expected == actual , "title mismatch"
# driver.find_element(By.XPATH, '//textarea[@title="Search"]').send_keys("gojo")
# driver.quit()

#_----------------------------------------------------------------------------------------------------------------######

# driver.get("https://www.amazon.in/")
# driver.find_element(By.XPATH, '//a[. = "Bestsellers"]').click()


# driver.save_screenshot('screenshot1.png')                                               # in same folder
# driver.save_screenshot(r"C:\Users\ADITYA\Downloads\screenshot.png")                    # by path

##Another System
# folder = os.path.join(os.getcwd(), 'screensht')
# os.makedirs(folder, exist_ok=True)
#
# # driver.save_screenshot(f'{folder}/screensht.png')
#
# ## for taking the screenshot of a particular element
# ele = driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
# # ele.screenshot(os.path.join(folder, "screenshot.png"))
# timestamps = time.strftime("%Y%m%d - %H%M%S")
# ele.screenshot(os.path.join(folder, f"screenshot{timestamps}.png"))

########################################################################################################################
driver.get("https://www.saucedemo.com/")

# driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
# driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("asdfg")
# driver.find_element(By.XPATH, '//input[@id="login-button"]').click()
#
# try:
#     actual = driver.current_url
#     excepted = "https://www.saucedemo.com/inventory.html"
#     assert actual == excepted
#     print("Test passed")
#
# except AssertionError:
#     # driver.save_screenshot("screenshot2.png")
#     folder = os.path.join(os.getcwd(), 'screensht')
#     os.makedirs(folder, exist_ok=True)
#     driver.save_screenshot(f'{folder}/screensht.png')

########################################################################################################################

actions = ActionChains(driver)

