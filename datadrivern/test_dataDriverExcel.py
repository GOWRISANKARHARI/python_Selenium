import pytest
import test
from selenium import webdriver
from selenium.webdriver.common.by import By
from utlitity import excelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username,password", excelReader.get_data("D:\\pythonselenium\\assignmentSeleniumPython\\ass\\datadrivern\\excel\\li.xlsx", "Sheet1"))
class TestLogin:
    def test_validlogin(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.find_element(By.ID, value="login2").click()
        self.driver.find_element(By.ID, value="loginusername").send_keys(username)
        self.driver.find_element(By.ID, value="loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, value="//button[contains(text(),'Log in')]").click()
        if(username == "admin"):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logout2")))
            assert self.driver.find_element(By.ID, "logout2").is_displayed()
        else:
            WebDriverWait(self.driver,10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert "Wrong password." in alert.text
            alert.accept()

        