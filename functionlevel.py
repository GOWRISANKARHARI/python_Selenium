#hard assert code 
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# def setup_function(function):
#     global driver
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://omayo.blogspot.com/")

# def teardown_function(function):
#     driver.quit()

# def test_senddata():
#     textarea = driver.find_element(By.XPATH, '//*[@id="ta1"]')
#     input_text = "WE ARE PLAYING FOR SOME TIME WITH OUR FRIENDS FOR SOME TIME"
#     textarea.send_keys(input_text)

#     sent = textarea.get_attribute("value")
#     print(sent)


#     assert sent == "\n" + input_text

#soft assert 

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_function(function):
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

def teardown_function(function):
    driver.quit()

def test_register_page():
    driver.find_element(By.LINK_TEXT, value = "Register").click()
    driver.find_element(By.NAME, value = "customer.firstName").send_keys("hari")
    driver.find_element(By.NAME, value = "customer.lastName").send_keys("s")
    driver.find_element(By.NAME, value = "customer.address.street").send_keys("1234")
    driver.find_element(By.NAME, value = "customer.address.city").send_keys("IND")
    driver.find_element(By.NAME, value = "customer.address.state").send_keys("TN")
    driver.find_element(By.NAME, value = "customer.address.zipCode").send_keys("10001")
    driver.find_element(By.NAME, value = "customer.phoneNumber").send_keys("1234567890")
    driver.find_element(By.NAME, value = "customer.ssn").send_keys("12312")
    driver.find_element(By.NAME, value = "customer.username").send_keys("hari12345")
    driver.find_element(By.NAME, value = "customer.password").send_keys("h@0715")
    driver.find_element(By.NAME, value = "repeatedPassword").send_keys("h@0715")
    driver.find_element(By.XPATH, value = "//input[@value='Register']").click()

def test_login_page():
    driver.find_element(By.NAME, value = "username").send_keys("k")
    driver.find_element(By.NAME, value = "password").send_keys("k@0715")
    driver.find_element(By.XPATH, value = "//input[@value='Log In']").click()
    assert driver.find_element(By.XPATH, value = "//div[@id='showOverview']/h1").is_displayed()