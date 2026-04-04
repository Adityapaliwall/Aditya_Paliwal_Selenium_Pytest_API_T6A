from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/ ")
driver.maximize_window()
actions = ActionChains(driver)

hov = driver.find_element(By.XPATH, '//button[. = "Point Me"]')
actions.move_to_element(hov).pause(2).perform()

do_tt = driver.find_element(By.XPATH, '//button[. = "Copy Text"]')
actions.double_click(do_tt).pause(2).perform()

dragg = driver.find_element(By.XPATH, '//div[@id="draggable"]')
dropp = driver.find_element(By.XPATH, '//div[@id="droppable"]')
actions.drag_and_drop(dragg, dropp).pause(3).perform()

driver.quit()