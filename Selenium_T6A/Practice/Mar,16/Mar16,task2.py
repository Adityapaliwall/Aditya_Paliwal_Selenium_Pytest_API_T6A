from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(1)

driver.find_element(By.CLASS_NAME, "nw1UBF.v1zwn25").send_keys("Mobiles")

sleep(2)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
sleep(2)

# driver.find_element(By.XPATH, '(//div[text() = "Samsung Galaxy F06 5G (Bahama Blue, 64 GB)"]/../../..//div)[19]')
print(driver.find_element(By.XPATH, '(//div[text() = "Samsung Galaxy F06 5G (Bahama Blue, 64 GB)"]/../../..//div)[19]').text)

sleep(1)
driver.quit()
