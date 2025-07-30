from selenium import webdriver
import pytest
from config import URL


@pytest.fixture
def driver():
    # username = "hemeshreddy_FNKLZ0"
    # key = "pCTKSD4cMEobz8WnvTPt"
    # caps = {
    #     "os": "Windows",
    #     "os_version": "7",
    #     "browser": "Firefox",
    #     "browser_version": "107",
    # }
    # options = webdriver.FirefoxOptions()
    # for cap_key, cap_value in caps.items():
    #     options.set_capability(cap_key, cap_value)
    # driver = webdriver.Remote(
    #     command_executor=f"https://{username}:{key}@hub-cloud.browserstack.com/wd/hub",
    #     options=options
    # )
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()
