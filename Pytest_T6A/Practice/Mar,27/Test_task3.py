from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()
actions = ActionChains(driver)

def test_web():
    driver.get("https://demowebshop.tricentis.com/")

def test_scrool():
    ele = driver.find_element(By.XPATH, '//li[@class="facebook"]')
    actions.scroll_to_element(ele).perform()

def test_facebook():
    driver.find_element(By.XPATH, '//li[@class="facebook"]//a').click()

def test_switch():
    driver.switch_to.window(driver.window_handles[1])

def test_us_nm():
    driver.find_element(By.XPATH, '(//input[@name="email"])[2]').send_keys("abc@gmail.com")

def test_pass():
    driver.find_element(By.XPATH, '(//input[@name="pass"])[2]').send_keys("123qweasd")

def test_log():
    driver.find_element(By.XPATH, '(//span[contains(text() , "Log in")])[3]').click()

def test_quit():
    driver.quit()
