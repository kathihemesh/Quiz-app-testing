import requests
import pytest
from config import API_URL
import pytest_check as check


def test_fetch_questions_success():
    params = {
        "amount": 10,
        "difficulty": "easy",
        "type": "multiple",
        "category": 9
    }
    response = requests.get(API_URL, params=params)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    check.equal(data["response_code"], 0, f"Response code is not 0, got {data['response_code']}")
    check.equal(len(data["results"]), 10, f"Did not receive 10 results, got {len(data['results'])}")
    for question in (data["results"]):
        check.is_true("question" in question, "'question' key missing")
        check.is_true("correct_answer" in question, "'correct_answer' key missing")
        check.is_true("incorrect_answers" in question, "'incorrect_answers' key missing")
        check.equal(len(question["incorrect_answers"]), 3, f"Incorrect answers count is not 3, got {len(question['incorrect_answers'])}")