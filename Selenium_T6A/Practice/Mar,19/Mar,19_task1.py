from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless")
driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Watches")
driver.find_element(By.ID, "nav-search-submit-button").click()

lis = driver.find_elements(By.XPATH, '(//img[@class ="s-image"])')
# l1 = driver.find_elements(By.TAG_NAME, "a")

print(len(lis))
for i in range(0, len(lis)):
    if i == 5:
        lis[i].click()


