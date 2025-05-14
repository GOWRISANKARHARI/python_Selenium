import pytest
from selenium.webdriver.common.by import By
import read_config
import time
import excelReader

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("username , password",excelReader.get_datas("D:\\pythonselenium\\assignmentSeleniumPython\\ass\\datadriven_assignes_pro\\Excel\\data.xlsx","Sheet1"))
class TestLogin:
    def test_valid(self,username,password):
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID,"login-button").click()