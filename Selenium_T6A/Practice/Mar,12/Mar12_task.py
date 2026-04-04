from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.wikipedia.org/")
driver.refresh()
print(driver.title)
sleep(3)
driver.get("https://amazon.in/")
sleep(3)
print(driver.title)
driver.back()
sleep(3)
driver.close()