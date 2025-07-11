from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.quiz_page import QuizPage
from pages.home_page import home
import pytest_check as check


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
        check.is_true(quiz_page.get_quiz_section().is_displayed(), "Failed to navigate to quiz section")
        quiz_page.click_option(1)
        time.sleep(1)
        feedback = quiz_page.get_feedback()
        check.is_true(feedback in ["Correct!", "Wrong!"], "Feedback is not displayed")
        time.sleep(1)
        quiz_page.click_next()
        time.sleep(1)
        check.is_true(quiz_page.get_question() != prev_question, "Question did not change")
        time.sleep(1)
        quiz_page.click_home()
        time.sleep(2)
        check.is_true(homepage.get_heading().is_displayed(), "Failed to navigate to home page")
