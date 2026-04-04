'''
XPATH
XML Path
        -> We can traverse backward and forward
        -> Locate elements based on text
        > Locate elements based on attribute
        -> used for dynamic elements

    Types of Xpath method:
                        -> Absolute
                                    -> it will start with / operator and from root node traverse to the elements

                        ->Relative
                                    -> it will start with // and directly goes to elements
                                    -> //tagname [@attribute = 'value']

    XPath using attribute               //tagname[@attribute = 'value']
    Xpath using text                    //tagname[. = "Submit"]
    XPath using contains attribute      //tagname[contains(@attribute, 'value')]
    XPath using contain  text           //tagname[contains(. = "Submit")]  |or|  //tagname[contains(text() = "Submit")]
'''
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

########################################################################################################################
## XPath                 (using attribute)   //tagname[@attribute = 'value']

# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.XPATH, '//input[@placeholder="Full Name"]').send_keys("Aditya")
# driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]').send_keys("asdlfkj@gmail.com")
# driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]').send_keys("why do you need")
# driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys("why do you need")
# driver.find_element(By.XPATH,'//button[@id="submit"]').click()
#
# sleep(2)
# driver.quit()


###########             #######################                         ##############          ################
# Xpath     (using text)        //tagname[. = "Submit"]
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.XPATH, '//input[@placeholder="Full Name"]').send_keys("Aditya")
# driver.find_element(By.XPATH,'//button[.="Submit"]').click()
# sleep(1)
# driver.quit()


#-------------------------------------------------------
# driver.get("https://amazon.in")
# driver.maximize_window()
# sleep(2)
#
# driver.find_element(By.XPATH, '//a[text()="Bestsellers"]').click()
# sleep(2)
# driver.quit()

########-----------------------#############################----------------------------------#########################
##XPath         (XPath using contains attribute )        //tagname[contains(@attribute, 'value')]

# driver.get("https://amazon.in")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.XPATH, '//a[contains(@href, "https://accelerator.")]').click()
# sleep(3)
# driver.quit()

###############-----------------####################-------------------------------####################################
## XPath  (XPath using contains text)   //tagname[contains(. = "Submit")]  |or|  //tagname[contains(text() = "Submit")]

#
# driver.get("https://amazon.in")
# driver.maximize_window()
# sleep(1)
#
# driver.find_element(By.XPATH, '//a[contains(text() ,"Sell under Amazon Accelerator")]').click()
# # driver.find_element(By.XPATH, '//a[contains(. ,"Sell under Amazon Accelerator")]').click()
# sleep(3)
# driver.quit()


#######################################################################################################################
## Group BY Indexing
'''
                            --> indexing start from 1 in selenium
                            
'''

## try

driver.get("https://chatgpt.com/")
driver.maximize_window()
sleep(2)

driver.find_element(By.XPATH, '//p[@data-placeholder ="Ask anything" ]').send_keys("tell me about yourself")
sleep(2)
# driver.find_element(By.XPATH, '//button[.//use[contains(@href,"sprites-core")]]').click()
driver.find_element(By.XPATH, '//button[@id="composer-submit-button"]').click()

sleep(2)
