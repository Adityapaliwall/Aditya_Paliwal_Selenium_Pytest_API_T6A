from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
actions = ActionChains(driver)

driver.find_element(By.XPATH, '//span[. = "✕"]').click()

scr = driver.find_element(By.XPATH, '//div[text() = "GROUP COMPANIES"]')
actions.scroll_to_element(scr).pause(2).perform()

driver.find_element(By.XPATH, '//a[text() = "Myntra"]').click()
actions.pause(3).perform()
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.XPATH, '//a[text() = "Shopsy"]').click()
actions.pause(3).perform()
driver.switch_to.window(driver.window_handles[0])

wind = driver.window_handles

for i in wind:
    driver.switch_to.window(i)

    print("Title: ", driver.title )
    print("URL: ", driver.current_url)
    print("Window_ID: ", i)
    print("_____________\n")


driver.quit()

