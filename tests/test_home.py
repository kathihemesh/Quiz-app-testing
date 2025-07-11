from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.home_page import home
import pytest_check as check


class TestHome():
    def test_ui(self, driver):
        home_page = home(driver)
        check.is_true(home_page.get_heading().is_displayed(), "Heading is not displayed")
        check.is_true(home_page.get_high_score().is_displayed(), "High Score label is not displayed")
        check.is_true(home_page.get_category().is_displayed(), "Category dropdown is not displayed")
        check.is_true(home_page.get_difficulty().is_displayed(), "Difficulty dropdown is not displayed")
        check.is_true(home_page.get_no_of_questions().is_displayed(), "Number of Questions dropdown is not displayed")
        home_page.click_start()
        time.sleep(2)
        check.is_true(home_page.get_quiz_section().is_displayed(), "Quiz section is not displayed after clicking start")
        time.sleep(1)