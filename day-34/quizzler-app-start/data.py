import requests
API_URL="https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean"

response = requests.get(API_URL)
data = response.json()

question_data = []

for question in data["results"]:
    question_data.append({
        "category": question["category"],
        "type": question["type"],
        "difficulty": question["difficulty"],
        "question": question["question"],
        "correct_answer": question["correct_answer"],
        "incorrect_answers": question["incorrect_answers"]
    })
