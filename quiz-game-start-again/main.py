from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    question_text = dictionary["text"]
    answer_text = dictionary["answer"]
    new_question = Question(question_text, answer_text) # new object created
    question_bank.append(new_question)                  # list of objects

# print(question_bank)
# print(question_bank[0].text)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")