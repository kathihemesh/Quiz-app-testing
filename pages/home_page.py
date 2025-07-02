from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class home():
    category="#category"
    difficulty="#difficulty"
    no_of_questions="#questionCountSelect"
    start="#startButton"
    quiz="#quizSection"
    def __init__(self,driver):
        self.driver=driver
    def get_category(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.category)
    def get_difficulty(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.difficulty)
    def get_no_of_questions(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.no_of_questions)
    def select_category(self,category):
        select=Select(self.driver.find_element(By.CSS_SELECTOR,self.category))
        select.select_by_value(category)
    def select_difficulty(self,difficulty):
        select=Select(self.driver.find_element(By.CSS_SELECTOR,self.difficulty))
        select.select_by_value(difficulty)
    def select_no_of_questions(self,no_of_questions):
        select=Select(self.driver.find_element(By.CSS_SELECTOR,self.no_of_questions))
        select.select_by_value(no_of_questions)
    def click_start(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.start))
        ).click()
    def get_heading(self):
        return self.driver.find_element(By.XPATH,"//h1[text()='Quiz App']")
    def get_high_score(self):
        return self.driver.find_element(By.XPATH,"//div[contains(text(),'High Score')]")
    def get_quiz_section(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.quiz)