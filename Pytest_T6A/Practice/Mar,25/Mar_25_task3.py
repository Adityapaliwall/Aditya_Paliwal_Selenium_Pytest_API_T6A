from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("Mobiles")
sel = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="s-suggestion-container"])[4]')))
sel.click()
driver.find_element(By.XPATH, '//span[@id="a-autoid-0-announce"]').click()
driver.find_element(By.XPATH, '//a[. = "Newest Arrivals"]').click()
driver.find_element(By.XPATH, '//span[. = "Free Shipping"]').click()
name = driver.find_element(By.XPATH, '(//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"])[1]')
print(f'Phone name: {name.text}')
price = driver.find_element(By.XPATH, '(//span[@class="a-price"])[1]')
print(f'Price: {price.text}')

driver.quit()

