from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
driver.maximize_window()

l1 = driver.find_elements(By.XPATH, '//li[@class="nav-li"]//a')

print(len(l1))

for i in range(len(l1)):
    print(f"{l1[i].text} -> {l1[i].get_attribute('href')}")

driver.quit()