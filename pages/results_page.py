from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ResultsPage():
    final_score = "#finalScore"
    retry_button = "#retryButton"
    home_button = "#homeButton"
    comment="performanceFeedback"
    def __init__(self,driver):
        self.driver = driver
    def get_final_score(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.final_score).text
    def click_retry(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.retry_button))
        ).click()
    def click_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.home_button))
        ).click()
    def get_comment(self):
        return self.driver.find_element(By.ID, self.comment)
