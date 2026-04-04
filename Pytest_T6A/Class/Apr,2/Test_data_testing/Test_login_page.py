import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from Test_data_retrival import test_fun1
# from conftest import test_openChrome




@pytest.mark.parametrize("username, password", test_fun1())
def test_sauce_login(test_openChrome, username, password):
    driver = test_openChrome

    actual = "https://www.saucedemo.com/inventory.html"

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    assert driver.current_url == actual
    print("test passed")