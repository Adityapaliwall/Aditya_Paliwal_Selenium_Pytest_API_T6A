from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.wikipedia.org/")
sleep(1)
driver.refresh()
print(driver.title)

driver.get("https://www.amazon.com/")
sleep(1)
print(driver.title)

driver.back()
sleep(1)
driver.close()