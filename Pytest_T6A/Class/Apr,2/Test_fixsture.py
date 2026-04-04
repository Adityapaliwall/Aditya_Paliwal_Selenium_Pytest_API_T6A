"""
In built Marker are: -> @pytest.mark.skip
                     -> @pytest.mark.skipif(False, reason="Not working")

Parameterise Marker: -> @pytest.mark.parametrize(data, [values])

"""
from tkinter.scrolledtext import example

import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# o.add_argument("--disable-notifications")
# driver = Chrome(options=o)
# driver.implicitly_wait(10)


###############################################################################################################################

# class Test_Demo:
#     @pytest.mark.skip
#     def test_login(self):
#         print("Logging in...")
#         assert 'hello' == 'hello'
#         assert 'world' == 'world'
#
#     @pytest.mark.smoke
#     def test_logout(self):
#         print("Logging out...")
#         ls = [1,2,3,4,5]
#         2 in ls
#         print( 2 in ls)
#
#     @pytest.mark.regression
#     # @pytest.mark.skipif(reason="Not working")
#     def test_register(self):
#         print("Logging in...")
#         ls = [1, 2, 3, 4, 5]
#         assert (2 in ls) == True
#
#     @pytest.mark.parametrize("a,b", [(1,2), (3,4)])
#     def test_add(self,a,b):
#         print(a+b)

#############################################################################################################################


# driver.maximize_window()
#
# @pytest.mark.parametrize("username, password", [("standard_user","secret_sauce"), ("standard_user","secret_sauce")])
# def test_demo_login(username, password):
#
#     driver.implicitly_wait(10)
#     autal = "https://www.saucedemo.com/inventory.html"
#     driver.get("https://www.saucedemo.com/")
#     driver.maximize_window()
#     driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys(username)
#     driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
#     driver.find_element(By.XPATH, '//input[@id="login-button"]').click()
#     assert driver.current_url == autal
#     print("test passed")
#
# #
# def test_quit():
#     driver.quit()

####################################################################################################################################
## fixture simple example()

# @pytest.fixture
# ### @pytest.fixture(autouse=True)       ### to work for all functions
# def greet():
#     print("hello al!")
#     yield
#     print("Bye")
#
# def test_morning(greet):
#     print("Good morning!")
#
# def test_evening():
#     print("Good evening!")

####################################################################################################################################

##Above question with fixture
import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

@pytest.fixture
def test_openChrome():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    o.add_argument("--disable-notifications")
    driver = Chrome(options=o)
    driver.implicitly_wait(10)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()


    yield driver

    print("Closing the driver")
    driver.quit()


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),("standard_user", "secret_sauce")])
def test_sauce_login(test_openChrome, username, password):
    driver = test_openChrome

    actual = "https://www.saucedemo.com/inventory.html"

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    assert driver.current_url == actual
    print("test passed")