'''
there are two method to find the elements:
                1. find_element(locator_name,locator_value) ->
                                -> it takes two arguments, this is for single elements
                                -> this return one single web element
                                -> if element is not found it will show "No Such Element Exception"
                                
                2. find_elements(locator_name,locator_value) ->
                                ->  it also take two arguments, this is for multiple elements
                                -> it return list of web elements
                                -> if element is not found it will show "Empty List"
    ## Locators: 
                = address of an elements
         -> Types of locators:
          ---1. ID              5. LINK TEXT          ------\   Text
 Direct  /   2. NAME            6. PARTIAL LINK TEXT  ------|   Based
 Locator \   3. CLASS_NAME       7. CSS SELECTORS    ------\
          ---4. TAG NAME        8. XPATH             ------/     Expression Based Locators
    
    ##  Action Perfored on the elements are:
            1. click() -> to click on the web elements(basic mouse uses)
            2. send_keys('text')  -> to enter the input in the web 
                                
'''

from time import sleep
from webbrowser import Chrome

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

#######################################################################################################################
# ID LLocator#


## submit data into a form
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(2)
#
# driver.find_element(By.ID, "userName").send_keys("Archit Sasxena")  ## select by id locator and giving text by sned.click
# email = driver.find_element(By.ID, "userEmail",)
# email.send_keys("f321465498sd@gmail.com")
# driver.find_element(By.ID, "currentAddress").send_keys("Archit Sasxena sdfhj, ,sd,fdsf, a,f,w f,dsaf, sdf, ds,fasd,fad,sf,f v")
# driver.find_element(By.ID, "permanentAddress").send_keys("why do you need the addrress")
# driver.find_element(By.ID, "submit").click()

## search into amazon
# driver.get("https://amazon.com")
# driver.maximize_window()
#
# sleep(1)
# driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Shirts")
#
# driver.find_element(By.ID, "nav-search-submit-button").click()

#######################################################################################################################
## Name

# driver.get("https://amazon.com")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.NAME, "field-keywords").send_keys("shirts")
# sleep(1)
# driver.find_element(By.ID, "nav-search-submit-button").click()

###################################################################################################################
## CLass

# driver.get("https://amazon.com")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.CLASS_NAME, "nav-input.nav-progressive-attribute").send_keys("shirts")
# sleep(1)
# driver.find_element(By.ID, "nav-search-submit-button").click()
#
# sleep(3)
# driver.close()

#####################################################################################################################
## TAG NAME

# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.TAG_NAME, "input").send_keys("Aditya")
# driver.find_element(By.TAG_NAME, "input").send_keys("Aditya@gmail.com")
# driver.find_element(By.TAG_NAME, "textarea").send_keys("Adityadfjs kadhjsf aksdhfj kadshfj ")
# driver.find_element(By.TAG_NAME, "textarea").send_keys("Aditya why od you need my address")
# driver.find_element(By.TAG_NAME, "button").click()
# driver.quit()

######################################################################################################################
## LINK TEXT   (work only work link tag only)

# driver.get("https://amazon.in")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.LINK_TEXT,"Sell").click()
# sleep(2)
# driver.quit()

######################################################################################################################
## PARTIAL LINK TEST  this is also only for ankor tag

# driver.get("https://amazon.in")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.PARTIAL_LINK_TEXT, "Pay").click()
# sleep(1)
# driver.quit()

######################################################################################################################
## CSS SELECTORS

driver.get("https://amazon.in")
driver.maximize_window()
sleep(1)

driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Amazon.in"]').send_keys("shirts")
sleep(1)
driver.quit()


