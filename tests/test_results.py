from selenium.webdriver.common.by import By
import time
import pytest
from pages.home_page import home
from pages.quiz_page import QuizPage
from pages.results_page import ResultsPage

# Helper function to complete quiz, track correct answers, and go to results page
def complete_quiz_and_go_to_results(driver):
    home_page = home(driver)
    home_page.select_no_of_questions("10")
    home_page.click_start()
    time.sleep(1)
    quiz_page = QuizPage(driver)
    correct_count = 0
    for i in range(10):
        quiz_page.click_option(2)
        time.sleep(0.3)
        
        feedback = quiz_page.get_feedback()
        if "correct" in feedback.lower():
            correct_count += 1
        quiz_page.click_next()
        time.sleep(0.3)
    results_page = ResultsPage(driver)
    return results_page, correct_count

def test_retry_quiz(driver):
    results_page, correct_count = complete_quiz_and_go_to_results(driver)
    time.sleep(2)
    # Check high score matches correct answers
    results_page=ResultsPage(driver)
    high_score = results_page.get_final_score()
    assert high_score == str(correct_count), f"High score ({high_score}) does not match correct answers ({correct_count}) after quiz."
    results_page.click_retry()
    quiz_page = QuizPage(driver)
    assert quiz_page.get_quiz_section().is_displayed(), "Quiz section is not displayed after retrying quiz"

def test_home_button(driver):
    results_page, correct_count = complete_quiz_and_go_to_results(driver)
    time.sleep(2)
    results_page=ResultsPage(driver)
    high_score = results_page.get_final_score()
    assert high_score == str(correct_count), f"High score ({high_score}) does not match correct answers ({correct_count}) after quiz."
    results_page.click_home()
    time.sleep(2)
    home_page = home(driver)
    assert home_page.get_heading().is_displayed(), "Home heading is not displayed after clicking home button"
