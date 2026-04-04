from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.XPATH,'//input[@class="sc-dBfaGr dyyfrm"]').send_keys("Roti")
driver.find_element(By.XPATH,'//input[@class="sc-dBfaGr dyyfrm"]').click()


dishes = driver.find_elements(By.XPATH,'//div[@class="sc-glUWqk GrjUP"]')

for i in dishes:
    print(i.text)
dishes[1].click()

driver.quit()
