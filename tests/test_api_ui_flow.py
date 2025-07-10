import time
import pytest
import html
from pages.home_page import home
from pages.quiz_page import QuizPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class window_api_response_available:
    def __call__(self, driver):
        return driver.execute_script("return typeof window.apiResponse !== 'undefined' && window.apiResponse !== null;")


def test_api_ui_question_and_answer_match(driver):
    # Step 1: Start quiz via UI
    home_page = home(driver)
    home_page.select_category("9")  
    home_page.select_difficulty("easy")
    home_page.select_no_of_questions("10")
    time.sleep(3)
    home_page.click_start()
    time.sleep(1)
    quiz_page = QuizPage(driver)

    # Step 2: Wait for and get the exact API response used by the UI
    WebDriverWait(driver, 10).until(window_api_response_available())
    ui_api_response = driver.execute_script("return window.apiResponse;")
    api_questions = ui_api_response["results"]

    # Step 3: For each question, cross-check API and UI, select 2nd option, and compare correct answers before clicking next
    for i in range(10):
        api_question = (html.unescape(api_questions[i]["question"])).strip()
        " ".join(api_question.split())
        api_correct_answer = (html.unescape(api_questions[i]["correct_answer"])).strip()
        ui_question = quiz_page.get_question()
        assert api_question == ui_question, f"Mismatch: API='{api_question}' UI='{ui_question}'"
        quiz_page.click_option(1) 
        ui_correct_answer = quiz_page.get_correct_answer()
        assert api_correct_answer == ui_correct_answer, f"Correct answer mismatch: API='{api_correct_answer}' UI='{ui_correct_answer}'"
        quiz_page.click_next()

