from question_model import Question
from data import  generate_api_request
from quiz_brain import QuizBrain
from setup_screen import SetupScreen, get_parameters
from ui import QuizInterface

# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# Create an instance of SetupScreen
setup = SetupScreen()

# Run the Tkinter main loop to get user inputs
setup.window.mainloop()

# Get the parameters after the setup is completed
parameters = setup.get_parameters()

question_data = generate_api_request(parameters)

quiz = QuizBrain(question_data)

# Finally, create an instance of QuizInterface using the QuizBrain
quiz_interface = QuizInterface(quiz)




# setup = SetupScreen()
# print(setup.get_parameters())
# quiz = QuizBrain(question_bank)
# quiz_interface = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
