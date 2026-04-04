"""
Only three things are import by common --> by, key,action_chains

Wait are of three types:

    1. Implicit Wait : only find if the element is present or not in HTML /not it is executable or not
                -> Keep checking for elements for a fixed amount of time before throwing an error.
                -> it is also called global wait
                ->Selenium keeps checking again and again for the element.This is called Polling.
                -> Selenium checks for element every ~500 milliseconds (0.5 sec)
                -> Syntax --> driver.implicitly_wait(10)
                -> Implicit wait only checks if the element exists in the DOM, not whether it is visible or usable.
                -> it work for all find_element in the code

    2. Explicit Wait: Explicit wait tells the program to wait until a specific condition happens before moving ahead.
                -> Waits only when needed (faster than implicit wait)
                -> Can wait for specific conditions (visible, clickable, etc.)
                -> Synttax --> var= WebDriverWait(driver, sec).until(EC.condition((By.XPATH, "element_location")))
                -> EC == Expected Conditions


"""
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
#######################################################################################################################
## Locating the dynamic elements

# driver.implicitly_wait(15)
# driver.get("https://the-internet.herokuapp.com/dynamic_loading")
# driver.maximize_window()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Example 1: Element on page that is hidden").click()
# driver.find_element(By.XPATH, "//button[text() = 'Start']").click()
#
# print(driver.find_element(By.XPATH, "//div[@id = 'finish']").text)

#_____________________________________________________________________________________________________________________##
## example
# driver.implicitly_wait(10)
# driver.get("https://www.decathlon.in/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, '//a[@href="https://www.decathlon.in/shop/Winter-Collection"]').click()
#
# driver.find_element(By.XPATH, '//a[@href="https://www.decathlon.in/c/jackets-26192"]').click()

#########
#######################################################################################################################
## Explicit wait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://the-internet.herokuapp.com/dynamic_loading")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT, "Example 1: Element on page that is hidden").click()
driver.find_element(By.XPATH, "//button[text() = 'Start']").click()

txt = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Hello World!')])[4]")))

print(txt.text)

driver.quit()








