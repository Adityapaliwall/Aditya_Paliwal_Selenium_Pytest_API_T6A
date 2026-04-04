from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@id="singleFileInput"]').send_keys(r"C:\Users\ADITYA\Downloads\Problem_Statement_1.md")

# driver.find_element(By.XPATH, '//input[@id="multipleFilesInput"]').send_keys(r"C:\Users\ADITYA\Downloads\Problem_Statement_1.md")
# driver.find_element(By.XPATH, '//input[@id="multipleFilesInput"]').send_keys(r"C:\Users\ADITYA\Downloads\Problem_Statement_2.md")

driver.find_element(By.XPATH, '//input[@id="multipleFilesInput"]').send_keys(r"C:\Users\ADITYA\Downloads\Problem_Statement_2.md"+"\n"+r"C:\Users\ADITYA\Downloads\Problem_Statement_2.md")