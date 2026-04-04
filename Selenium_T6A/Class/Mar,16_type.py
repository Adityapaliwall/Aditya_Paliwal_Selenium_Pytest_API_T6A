"""
XPath: ->
        Traversing:
                -> traversing a web page
                -> there are two method of traversing
                             -> Forward :
                                        -> form the parent element child is fetched
                             -> Backward
                                        -> from child element parent is fetched
                -> Steps of traversing
                    ->First way of traversing
                        1. Indentify static elements
                        2. Move to common parent
                        3. From the common parent fetch the dynamic elements

        Sibling:
            -> Two types of Sibling:
                    -> Following sibling  : element next or after the static element
                                        -> Syntax ->
                    -> Preceding sibling  : element previous or above the static element
                                        -> Syntax ->



"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)               ## for holding the browser
# o.add_argument("--headless")                            ## for hiding the browser activity
# o.add_argument("--incognito")
driver = Chrome(options=o)

#######################################################################################################################
##locate using last name fetch the department
# driver.get("https://demoqa.com/webtables")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.XPATH, '//td[text() ="Vega"]/..//td[6]')
# print(driver.find_element(By.XPATH, '//td[text() ="Vega"]/..//td[6]').text)
#
# driver.quit()

###############---------------------#########---------------------------########-------------------------###############

# driver.get("https://the-internet.herokuapp.com/tables")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.XPATH, '//td[text() = "Frank"]/..//td[4]')
# print(driver.find_element(By.XPATH, '//td[text() = "Frank"]/..//td[4]').text)
# driver.quit()

######------------------------########_-----------------------------------------------######3-________________##########
## Sibling

# driver.get("https://the-internet.herokuapp.com/tables")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.XPATH, '//td[text() = "Tim"]//following-sibling::td[2]')
# print(driver.find_element(By.XPATH, '//td[text() = "Tim"]//following-sibling::td[2]').text)
# driver.quit()

######-------------________________________________________________________################______________________#######

driver.get("")
driver.maximize_window()
sleep(1)

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID, "nav-search-submit-button").click()
sleep(1)