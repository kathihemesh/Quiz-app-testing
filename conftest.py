from selenium import webdriver
import pytest
from config import URL
import logging

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()
