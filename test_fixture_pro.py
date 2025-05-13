
from selenium.webdriver.common.by import By
import pytest
import time
@pytest.mark.usefixtures("driver")
def test_Hp(driver):
    search_box = driver.find_element(By.XPATH, '//*[@class="gLFyf"]')
    search_box.send_keys("Hp")
    search_button = driver.find_element(By.XPATH, '(//*[@class="gNO89b"])[2]')
    search_button.click()
