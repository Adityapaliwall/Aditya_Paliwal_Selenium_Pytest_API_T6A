"""
Dropdowns--
Select Dropdowns- <select> </select>
 -select_by_visible_text
 -select_by_index
 -select_by_value

 for multi-select
 we can use deselect_by in multi-select

Custom Dropdown-
"""


from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)

# driver.get("https://www.amazon.in")
driver.get("https://www.zomato.com/jaipur/dine-out")
driver.maximize_window()
driver.implicitly_wait(10)

# dropdown = driver.find_element(By.ID,"state")
# multiselect = driver.find_element(By.ID,"hobby")
#
# option = Select(multiselect)
#
# # option.select_by_value("MH")
# # option.select_by_visible_text("Maharastra")
# option.select_by_index(1)
# option.select_by_index(0)
# option.select_by_value("yoga")
#
# option.deselect_by_index(0)
# option.deselect_all() for html code



# sleep(2)
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes for men")
# sleep(2)
# abc = driver.find_elements(By.XPATH,"//div[@class='s-suggestion-container']")
#
# for i in abc:
#     print(i.text)
# abc[3].click()

wait = WebDriverWait(driver, 10)
s = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@class='sc-dBfaGr dyyfrm']")))
s.send_keys("Dosa")
lst = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='sc-eQGPmX iLpcYt']")))
for i in lst:
    print(i.text)
sleep(5)
driver.quit()
#(//div[@class='s-suggestion s-suggestion-ellipsis-direction'])[1]