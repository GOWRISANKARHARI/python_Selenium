import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.mark.parametrize("browser", ["Chrome", "Firefox"])
@pytest.mark.parametrize("url",["https://www.amazon.in/","https://www.flipkart.com/"])
def test(browser,url):
    if(browser == "Chrome"):
        driver = webdriver.Chrome()
    if(browser == "Firefox"):
        driver = webdriver.Firefox()
    driver.get(url)
    print("url: ",driver.current_url)
    driver.quit()

#for startjj
@pytest.fixture()
def basic():
    global driver
    driver = webdriver.Firefox()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    yield 
    driver.quit()
def test_Hp(basic):
    driver.find_element(By.XPATH,value= '//*[@class="gLFyf"]').send_keys("Hp")
    # driver.find_element(By.XPATH,value='//*[@class="input-group"]/span').click()
    # ass = driver.find_element (By.XPATH,value='//div[@class="caption"]/h4/a').text
    # assert "HP LP3065" in ass

# def test_Honda(basic):
#     driver.find_element(By.XPATH,value= '//*[@class="input-group"]/input').send_keys("Honda")
#     driver.find_element(By.XPATH,value='//*[@class="input-group"]/span').click()
#     ass1 = driver.find_element(By.XPATH,'//*[@id="content"]/p[2]').text
#     assert "There is no product that matches the search criteria." in ass1

