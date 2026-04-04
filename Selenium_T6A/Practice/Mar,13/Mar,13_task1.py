from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://amazon.in")
driver.maximize_window()
sleep(2)

driver.find_element(By.ID, "glow-ingress-line2").click()
sleep(2)

driver.quit()

