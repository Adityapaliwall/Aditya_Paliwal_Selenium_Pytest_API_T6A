import pytest
from selenium.webdriver import Chrome, ChromeOptions

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