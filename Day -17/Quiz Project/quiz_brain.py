class QuizBrain:

    def __init__(self,list):
        self.question_number = 0
        self.score = 0
        self.question_list = list

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) :")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_answer,answer):

        if user_answer.lower() == answer.lower():
            self.score += 1 
            print("You are right ")
        else:
            print("You are wrong")
        print(f"The correct answer was : {answer}")  
        print(f"Your current score is : {self.score}/{self.question_number}")