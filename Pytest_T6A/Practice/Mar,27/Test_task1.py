from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

def test_website():
    driver.get("https://demowebshop.tricentis.com/")

def test_res_page():
    driver.find_element(By.XPATH, '//a[@class="ico-register"]').click()

def test_box():
    driver.find_element(By.XPATH, '//input[@id="gender-male"]').click()

def test_finame():
    driver.find_element(By.XPATH, '//input[@id="FirstName"]').send_keys("hello")

def test_lsname():
    driver.find_element(By.XPATH, '//input[@id="LastName"]').send_keys("Bye")

def test_email():
    driver.find_element(By.XPATH, '//input[@id="Email"]').send_keys("asd@gmail.com")

def test_pass():
    driver.find_element(By.XPATH, '//input[@id="Password"]').send_keys("123qwe@@")

def test_conpass():
    driver.find_element(By.XPATH, '//input[@id="ConfirmPassword"]').send_keys("123qwe@@")

def test_submit():
    driver.find_element(By.XPATH, '//input[@id="register-button"]').click()

def test_close():
    driver.quit()