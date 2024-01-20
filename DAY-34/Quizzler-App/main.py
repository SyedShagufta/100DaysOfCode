from question_model import Question
from data import  generate_api_request
from quiz_brain import QuizBrain
from setup_screen import SetupScreen, get_parameters
from ui import QuizInterface


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




