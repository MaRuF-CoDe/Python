from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new = Question(question_text,question_answer)
    question_bank.append(new)

quiz = QuizBrain(question_bank)

while quiz.still_has_question:
    quiz.next_question()
score = quiz.score
ques = quiz.question_number
print("You've completed the quiz")
print (f"Your final score is {score}/{ques}")