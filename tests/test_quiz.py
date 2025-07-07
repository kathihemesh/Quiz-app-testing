from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from pages.quiz_page import QuizPage
from pages.home_page import home
class TestQuiz():
    def test_ui(self, driver):
        homepage= home(driver)
        homepage.select_category("11")
        time.sleep(1)
        homepage.select_difficulty("medium")
        time.sleep(1)
        homepage.select_no_of_questions("20")
        time.sleep(1)
        homepage.click_start()
        time.sleep(2)
        quiz_page = QuizPage(driver)
        prev_question = quiz_page.get_question()
        assert quiz_page.get_quiz_section().is_displayed(), "Quiz section is not displayed"
        quiz_page.click_option(1)
        time.sleep(1)
        try:
            assert quiz_page.get_feedback() == "Correct!", "Feedback is not correct"
        except:
            assert quiz_page.get_feedback() == "Wrong!", "Feedback is not correct"
        time.sleep(1)
        quiz_page.click_next()
        time.sleep(1)
        assert quiz_page.get_question() != prev_question, "Question did not change"
        time.sleep(1)
        quiz_page.click_home()
        time.sleep(2)
        assert homepage.get_heading().is_displayed(), "Heading is not displayed on home page"
