"""
Form in selenium
    -> there are three method for interact with form
        -> is_displayed() --> Checks whether the element is visible on the webpage
        -> is_enabled() --> Checks whether the element is enabled (can be interacted with)
        -> is_selected() --> Checks whether the element is selected (used for radio buttons, checkboxes, etc.)
"""
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless")
driver = Chrome(options=o)
# driver.implicitly_wait(10)

#######################################################################################################################

# driver.implicitly_wait(10)
# driver.get("https://google.com")
# driver.maximize_window()
#
# links = driver.find_elements(By.TAG_NAME, "a")
# print(links)
# for i in links:
#     print(i.text, end=" ")
# print(len(links))
# driver.quit()

#----------------------------------------------------------------------------------------------------------------------#

# driver.get("https://google.com")
# driver.maximize_window()
# ele = driver.find_element(By.XPATH, "//a[@class ='gb_A']")
# print(ele.get_attribute("aria-label"))

#######################################################################################################################

# driver.get("https://www.facebook.com")
# driver.maximize_window()
#
# btn = driver.find_element(By.XPATH, '//div[@aria-label="Log in"]')
# print(btn.is_displayed())
# print(btn.is_enabled())
#
# driver.quit()

#---------------______________________________________________________________________________________________________#

# driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
# driver.maximize_window()
#
# reg = driver.find_element(By.XPATH, '//button[@type ="submit"]')
# print(reg.is_displayed())
# print(reg.is_enabled())
#
# driver.quit()

#######################################################################################################################

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
#
#
# c1 = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
# c2 = driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]')
# print(c1.is_displayed())
# print(c1.is_selected())
# print(c2.is_displayed())
# print(c2.is_selected())
#
#
# driver.quit()

#######################################################################################################################

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

driver.find_element(By.ID, "firstName").send_keys("Aditya")
driver.find_element(By.ID, "lastName").send_keys("Paliwal")
driver.find_element(By.ID, "userEmail").send_keys("asd@asd.com")
driver.find_element(By.XPATH, '//input[@id="gender-radio-1"]').click()
driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys("0987654321")

driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
mon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//option[@value="7"]')))
mon.click()

driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
dat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[. = "15"]')))
dat.click()
driver.find_element(By.XPATH, '(//div[@class="form-check form-check-inline"])[5]').click()
driver.find_element(By.XPATH, '(//div[@class="form-check form-check-inline"])[6]').click()

driver.find_element(By.XPATH, '//input[@id="uploadPicture"]').send_keys(r"C:\Users\ADITYA\Downloads\Problem_Statement_1.md")

# driver.find_element(By.XPATH, '//input[@id="subjectsInput"]').send_keys("Maths")

driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]').send_keys("why d you nedd")

driver.find_element(By.XPATH, '//div[@class="css-1wy0on6"]').click()
driver.find_element(By.XPATH, '//input[@id="submit"]').click()

driver.find_element(By.XPATH, '//button[@id="submit"]').click()
