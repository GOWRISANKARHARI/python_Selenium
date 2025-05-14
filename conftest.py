# conftest.py or in the same file

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(params=["chrome","firefox","edge"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver= webdriver.Edge()
    else:
        print("invalid")
    driver.get("https://www.google.com/")
    time.sleep(2)

    yield driver
    driver.quit()
