"""
Action: click(), send_keys()

Action keys: there called by Keys Class
        ->Syntax = send_keys(Key.ENTER)


Action Chain CLass : it will  create an object then store the object only then it will perform by .perform() only
                ->   Instead of doing one action at a time (like click or type), you can combine actions
        -> 1. Create Object
        -> 2. Store action
        -> 3. Perform it by .perform()
                -> Syntax: actions = ActionChains(driver)
                            actions.click(single).perform()

Scroll -- >1. scroll_to_element
                            -> Syntax: actions.scroll_to_element(element).perform()
           2. scroll_by_amount()
                            -> Syntax: actions.scroll_by_amount(amount).perform()
           3. scroll_from_origin()
                            -> Syntax: actions.scroll_from_origin(origin).perform()
                            example: search_box = driver.find_element(By.ID, "twotabsearchtextbox")
                                    origin = ScrollOrigin.from_element(search_box)
                                    actions.scroll_from_origin(origin, 0, 1300).perform()

Hover to the element :
                Syntax -> actions.move_to_element(ho).perform()

Hold an element:
                Syntax -> actions.click_and_hold(hd).perform()

Drag and drop :
                Syntax -> actions.pause(2).drag_and_drop(dra, dop).perform()

## Tab Switching
Switch to another Tab or Window:
                               1.  to fetch the id of the current window or page -> Current_window_handle
                               2.  to know or fetch all the id of the tab -> window_handles [ give as list of all te address]
                               3.  to switch btw different window  -> switch_to.window(window_id)


"""
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

########################################################################################################################
## for enter key example with amazon

# driver.get("https://amazon.in")
# driver.maximize_window()
#
# # driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("mobiles").send_keys(Keys.ENTER)  can only be used in ACtion change class
# ele = driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
# ele.send_keys("Mobiles")
# ele.send_keys(Keys.ENTER)

#----------------------------------------------------------------------------------------------------------------------#
# copy and paste example

# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# curr = driver.find_element(By.ID, "currentAddress")
# curr.send_keys("why di you want")
# curr.send_keys(Keys.CONTROL + "a")
# curr.send_keys(Keys.CONTROL+ "c")
#
# per = driver.find_element(By.ID, "permanentAddress")
# per.send_keys(Keys.CONTROL+ "v")

#######################################################################################################################
# Action Chain CLass

# driver.get("https://demoqa.com/buttons")
# driver.maximize_window()
# # driver.find_element(By.XPATH, '//button[. = "Double Click Me"]').click()
# # driver.find_element(By.XPATH, '//button[. = "Right Click Me"]').click()
# # driver.find_element(By.XPATH, '//button[. = "Click Me"]').click()
#
# single = driver.find_element(By.XPATH, '//button[. = "Click Me"]')
# dou = driver.find_element(By.XPATH, '//button[. = "Double Click Me"]')
# ri_cl = driver.find_element(By.XPATH, '//button[. = "Right Click Me"]')
#
# actions = ActionChains(driver)
# # actions.click(single).perform()
# # # actions.click(dou).click(dou).perform()
# # actions.double_click(dou).perform()
# # # actions.send_keys(Keys.RIGHT).perform()
# # actions.context_click(ri_cl).perform()
# actions.click(single).double_click(dou).context_click(ri_cl).perform()

#----------------------------------------------------------------------------------------------------------------------#
## Scroll the web pages
# driver.get("https://amazon.in")
# driver.maximize_window()
#
# sc = driver.find_element(By.XPATH, '((//span[contains(. , "Up to 60% off | Best offers on kitchen")])[2]/../../../..//img)[1]')
# actions = ActionChains(driver)
#
# actions.scroll_to_element(sc).pause(3).click(sc).perform()
#
# #__________________________________________________________________________________________#
# ## Scroll by coordinate
# ## Hou much you want to scroll on the screen using x nd y
# actions.pause(3).scroll_by_amount(20,1200).click().perform()
#
# #___________________________________________________________________________________________#
# ## scroll by origin
#
# search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# origin = ScrollOrigin.from_element(search_box)
# actions.scroll_from_origin(origin, 0, 1300).perform()

########################################################################################################################
## hover of the mouse

# driver.get("https://amazon.in")
# driver.maximize_window()
#
# ho = driver.find_element(By.ID, "icp-nav-flyout")
# actions = ActionChains(driver)
# actions.move_to_element(ho).perform()

########################################################################################################################
## hold the mouse on a element

# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# driver.maximize_window()
# actions = ActionChains(driver)
# actions.pause(2).perform()
# driver.find_element(By.XPATH, '//span[@class="ng-tns-c2785778308-3 icon-cancel"]').click()
# driver.find_element(By.XPATH, '//input[@id="userName"]').send_keys("abcdefghijkl")
# pa = driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("alsdkfj2348afdh9")
#
# hd = driver.find_element(By.XPATH, '(//img[@class="ng-star-inserted"])[1]')
# actions.click_and_hold(hd).pause(3).release().perform()

#######################################################################################################################
## Drag and drop

# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# actions = ActionChains(driver)
#
# dra = driver.find_element(By.XPATH, '//div[@id="draggable"]')
# dop = driver.find_element(By.XPATH, '//div[@id="droppable"]')
# actions.pause(2).drag_and_drop(dra, dop).perform()

########################################################################################################################
##Tab and Window Switching

driver.get("https://google.com")
driver.maximize_window()
actions = ActionChains(driver)
sleep(1)

print(driver.current_window_handle)
print(driver.title)

driver.switch_to.new_window()
print(driver.window_handles)

driver.get("https://amazon.in")
actions.pause(2).perform()
print(driver.title)
print(driver.current_window_handle)

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.PARTIAL_LINK_TEXT, "About").click()



actions.pause(3).perform()
driver.quit()



