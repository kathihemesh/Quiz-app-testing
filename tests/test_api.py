import requests
import pytest
from config import API_URL

def test_fetch_questions_success():
    params = {
        "amount": 10,
        "difficulty": "easy",
        "type": "multiple",
        "category": 9  # General Knowledge
    }
    response = requests.get(API_URL, params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["response_code"] == 0
    assert len(data["results"]) == 10
    for question in data["results"]:
        assert "question" in question
        assert "correct_answer" in question
        assert "incorrect_answers" in question
        assert len(question["incorrect_answers"]) == 3
