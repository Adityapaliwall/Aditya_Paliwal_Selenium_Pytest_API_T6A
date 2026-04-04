from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

def test_web():
    driver.get("https://demowebshop.tricentis.com/")

def test_pages():
    driver.find_element(By.XPATH, '//a[contains(. , "Apparel & Shoes")]').click()

def test_op1():
    dropp = driver.find_element(By.XPATH, '//select[@id="products-orderby"]')
    option = Select(dropp)
    option.select_by_index(1)

def test_op2():
    dp2 = driver.find_element(By.XPATH, '//select[@id="products-pagesize"]')
    option = Select(dp2)
    option.select_by_index(1)

def test_op3():
    dp3 = driver.find_element(By.XPATH, '//select[@id="products-viewmode"]')
    option = Select(dp3)
    option.select_by_index(1)

def test_cl():
    driver.quit()