"""
iFrame : an iframe is basically a webpage embedded inside another webpage.
        -> Selenium cannot directly interact with elements inside an iframe unless you first switch into it.

        -> in three ways we can switch in iframe
                1. using Index -> driver.switch_to.frame(0)
                2. using web element or locator -> driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="frame1"]'))
                3. using id name  -> driver.switch_to.frame("frame1")

Going back in Frame : going back to the previous or original frame
                    -> there are two method for this
                            1. Back to parent frame: -> driver.switch_to.parent_frame()
                            2. Back to main content: -> driver.switch_to.default_content()

## Alter
Alert and POP UP : this are the element show on the webpage
                    -> there are 3 types of alert
                        1. Simple Alert : -> alert = driver.switch_to.alert
                        2. Confirmation Alert
                        3. Prompt Alert

                        alert = driver.switch_to.alert

                        alert.accept()     # Click OK
                        alert.dismiss()    # Click Cancel
                        alert.text         # Get alert text
                        alert.send_keys()  # Enter text (for prompt alert)
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_experimental_option("prefs", {"safebrowsing.enabled": True})      ## only for enable and disable safebrowsing
o.add_argument("--disable-notifications")      # diable notoifcation
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

#_____________________________________________________________________________________________________#
# driver.get("file:///D:/Selenium_T6A/Class/Mar,24/index.html")
# driver.find_element(By.XPATH, '//input[@placeholder="Main page input"]').send_keys("hello")
# driver.switch_to.frame(0)
#
# driver.find_element(By.XPATH, '//input[@placeholder="Page 2 input"]').send_keys("world")
# driver.switch_to.frame(0)
#
# driver.find_element(By.XPATH, '//input[@placeholder="Page 3 input"]').send_keys("sdfd")
#______________________________________________________________________________________________________________________#
## by Using Id and name

# driver.switch_to.frame("frame1")
# driver.find_element(By.XPATH, '//input[@placeholder="Page 2 input"]').send_keys("hey d =o you need this")
#
# driver.switch_to.frame("frame2")
# driver.find_element(By.XPATH, '//input[@placeholder="Page 3 input"]').send_keys("sdfd")

#______________________________________________________________________________________________________________________#
## Using Locaotrs and web element

# driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="frame1"]'))
# driver.find_element(By.XPATH, '//input[@placeholder="Page 2 input"]').send_keys("hey d =o you need this")
#
# driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="frame2"]'))
# driver.find_element(By.XPATH, '//input[@placeholder="Page 3 input"]').send_keys("sdfd")

#_____________________________________________________________________________________________________________________#
## going back in frames
# driver.switch_to.parent_frame()
# driver.find_element(By.XPATH, '//input[@placeholder="Page 2 input"]').clear()
# driver.find_element(By.XPATH, '//input[@placeholder="Page 2 input"]').send_keys("i am abackj")
#
# driver.switch_to.default_content()
# driver.find_element(By.XPATH, '//input[@placeholder="Main page input"]').send_keys("why are you here")

#######################################################################################################################
## alert handling
# driver.get("https://testautomationpractice.blogspot.com/")

# driver.find_element(By.XPATH, '//button[@id="alertBtn"]').click()
# driver.switch_to.alert.accept()

# driver.find_element(By.XPATH, '//button[@id="confirmBtn"]').click()
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

# driver.find_element(By.XPATH, '//button[@id="promptBtn"]').click()
# driver.switch_to.alert.send_keys("Aditya")
# driver.switch_to.alert.accept()

#______________________________________________________________________________________________________________________#
## upload and download
# driver.get("https://demoqa.com/upload-download")
# driver.find_element(By.XPATH, '//input[@label="Select a File"]').send_keys(r"C:\Users\ADITYA\Downloads\Problem_Statement_1.md")
# driver.find_element(By.XPATH, '//a[. = "Download"]').click()

#_____________________________________________________________________________________________________________________#
# ## downloading
# driver.get("https://www.python.org/downloads/")
# driver.find_element(By.XPATH, '(//a[. = "Python 3.14.3"])[4]').click()

#_____________________________________________________________________________________________________________________#
### easy my trip disable notification
# driver.get("https://www.easemytrip.com/")

########################################################################################################################
# ## date handling
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.find_element(By.XPATH, '(//input[@type="text"])[3]').click()
# driver.find_element(By.XPATH, '(//a[@tabindex="0"])[18]').click()
# driver.find_element(By.XPATH, '(//td[@class="ng-tns-c69-9 ng-star-inserted"])[24]').click()

#_____________________________________________________________________________________________________________________#

driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
driver.find_element(By.XPATH)
