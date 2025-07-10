from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QuizPage:
    quizsection = "#quizSection"
    options = ".options"
    next_button = "#nextButton"
    home_button = "#homeIconButton"
    question="#questionText"
    feedback="#answerFeedback"

    def __init__(self,driver):
        self.driver = driver

    def get_quiz_section(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.quizsection)

    def get_options(self):
        return self.driver.find_elements(By.CSS_SELECTOR,self.options)

    def click_next(self):
        button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.next_button))
        )
        button.click()

    def click_option(self, n):
        options = self.get_options()
        options[n].click()

    def click_home(self):
        self.driver.find_element(By.CSS_SELECTOR,self.home_button).click()

    def get_question(self): 
        return self.driver.find_element(By.CSS_SELECTOR,self.question).text
    
    def get_feedback(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.feedback).text
    
    def get_correct_answer(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".bg-green-500").text