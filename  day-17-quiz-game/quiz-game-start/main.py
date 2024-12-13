from itertools import count

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in question_data:
    # question_text = i["text"]
    question_text = i["question"]
    # answer_text = i["answer"]
    answer_text = i["correct_answer"]
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)

# print(question_bank,"\n", len(question_bank)) # test
# print(question_bank[0].text, question_bank[0].answer) #question and answer to 1st question

# for i in question_bank:
#     index = question_bank.index(i)
#     print(index, ":", question_bank[index].text, question_bank[index].answer)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")