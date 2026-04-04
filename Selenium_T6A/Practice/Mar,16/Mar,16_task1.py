from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)



driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID, "nav-search-submit-button").click()
sleep(1)

driver.find_element(By.XPATH, '//h2[contains(.,"Samsung Galaxy M07 Mobile (Black, 4GB RAM, 64GB Storage)")]').click()
print(driver.find_element(By.XPATH, '//h2[contains(.,"Samsung Galaxy M07 Mobile (Black, 4GB RAM, 64GB Storage)")]/../../..//span[contains(@class,"a-price-whole")]').text)


sleep(4)


