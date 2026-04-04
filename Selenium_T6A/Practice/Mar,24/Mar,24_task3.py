from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://google.com")
driver.switch_to.new_window()
driver.get("https://www.amazon.in/")
driver.switch_to.new_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.window(driver.window_handles[0])
wind = driver.window_handles
for w in wind:
    driver.switch_to.window(w)
    print("Page URL : ", driver.current_url)
    print("Title : ", driver.title)
    print("Window_ID : ", w )
    print("_______________ \n")

# driver.switch_to.window(driver.window_handles[2])
# driver.close()
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
go
##      OR

cls = driver.window_handles
for c in cls[1:]:
    driver.switch_to.window(c)
    driver.close()

sleep(10)
driver.quit()

