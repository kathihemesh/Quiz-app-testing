import time
import pytest
import html
from pages.home_page import home
from pages.quiz_page import QuizPage
from selenium.webdriver.support.ui import WebDriverWait
import pytest_check as check


class window_api_response_available:
    def __call__(self, driver):
        return driver.execute_script("return typeof window.apiResponse !== 'undefined' && window.apiResponse !== null;")


def test_api_ui_question_and_answer_match(driver):
    home_page = home(driver)
    home_page.select_category("9")  
    home_page.select_difficulty("easy")
    home_page.select_no_of_questions("10")
    time.sleep(3)
    home_page.click_start()
    time.sleep(1)
    quiz_page = QuizPage(driver)
    WebDriverWait(driver, 10).until(window_api_response_available())
    ui_api_response = driver.execute_script("return window.apiResponse;")
    api_questions = ui_api_response["results"]

    for i in range(10):
        api_question = (html.unescape(api_questions[i]["question"])).strip()
        api_question=" ".join(api_question.split())
        if i==6:
            api_question=api_question+"123"
        api_correct_answer = (html.unescape(api_questions[i]["correct_answer"])).strip()
        ui_question = quiz_page.get_question()
        check.equal(api_question, ui_question, f"{i}.Mismatch: API='{api_question}' UI='{ui_question}'")
        quiz_page.click_option(1)
        time.sleep(0.3)
        ui_correct_answer = quiz_page.get_correct_answer()
        check.equal(api_correct_answer, ui_correct_answer, f"{i}.Correct answer mismatch: API='{api_correct_answer}' UI='{ui_correct_answer}'")
        quiz_page.click_next()
        time.sleep(0.3)

