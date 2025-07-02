from selenium import webdriver
import pytest
from config import URL
@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()
