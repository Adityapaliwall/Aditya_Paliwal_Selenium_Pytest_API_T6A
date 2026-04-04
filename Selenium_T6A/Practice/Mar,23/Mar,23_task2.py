from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.implicitly_wait(10)


driver.get("https://www.nike.com/")

driver.maximize_window()
actions = ActionChains(driver)

kid = driver.find_element(By.XPATH, '//span[. = "Kids"]')
actions.move_to_element(kid).pause(2).click().perform()

driver.switch_to.window(driver.window_handles[1])

scr = driver.find_element(By.XPATH, '//a[. = "Shop"]')
actions.scroll_to_element(scr).perform()
scr.click()

pr_sel = driver.find_element(By.XPATH, '(//div[@class="css-1sjxv95"])[4]')
actions.move_to_element(pr_sel).scroll_to_element(pr_sel).pause(1).click().perform()

driver.switch_to.window(driver.window_handles[2])

driver.find_element(By.XPATH, '//label[. = "UK 6 (EU 40)"]').click()
driver.find_element(By.XPATH, '//button[. = "Add to Bag"]').click()

actions.pause(3).perform()
driver.quit()

