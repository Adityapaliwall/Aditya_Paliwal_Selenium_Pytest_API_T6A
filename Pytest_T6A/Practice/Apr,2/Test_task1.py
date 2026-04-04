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