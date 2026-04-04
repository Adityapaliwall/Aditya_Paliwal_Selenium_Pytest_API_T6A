from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

"""
driver.find_element(By.XPATH, "//button[@id = 'addNewRecordButton']").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Aditya")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Paliwal")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH, "//input[@id='age']").send_keys("22")
# driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("52000")
# driver.find_element(By.XPATH, "//input[@id='department']").send_keys("Q&T")
# driver.find_element(By.XPATH, "//button[@id = 'submit']").click()
sala = driver.find_element(By.XPATH, "//td[text() = 'Aditya']/..//td[5]")
print("The Salary is:",sala.text)
"""

# driver.find_element(By.XPATH, "//button[@id = 'addNewRecordButton']").click()
name = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "(//tr)[5]//td[1]")))
salary = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "(//tr)[5]//td[5]")))

print(f" The Salary of {name.text} is {salary.text}")
driver.quit()

