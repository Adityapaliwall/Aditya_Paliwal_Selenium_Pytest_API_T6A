## for lauching in the browser chrome , Edge , Firefox

'''
## oopein ghthe browser and holding for 5 sec
from selenium.webdriver import Chrome
from time import sleep
driver  = Chrome()
sleep(5)
'''

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",False)
driver = Chrome(options=o)

## to open the webpage or website
# driver.get("https://google.com")
driver.get("https://demoqa.com/")

## to maximise the window it return type is none
# driver.maximize_window()
# sleep(2)

# ## fullscreen there will bo no task bar
# driver.fullscreen_window()
# sleep(3)

# ## for mini the window
# driver.minimize_window()

##--> to fetch the title of the web pages
title = driver.title
print(title)

##--> for printing link of the website in terminal
# print(driver.current_url)
# print(driver.page_source)

##--> to print the name of the browser
print(driver.name)

##--> in browser travel of backward, forward, and refresh


##--> for close the window
sleep(2)
driver.close()     ## it closes only the tab that open through this script other tab still remain open
# driver.quit()      ## it closes all the tab and entire-window


'''
from selenium.webdriver import Chrome, ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()

print(driver.title)

driver.back()
'''