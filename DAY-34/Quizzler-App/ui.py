from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # creating a window with a theme color
        self.window = Tk()
        self.window.title("Quizzer App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # create a score label
        self.score_label = Label(text=f"Score : 0", bg=THEME_COLOR, fg="white", font=("Bahnschrift", 15, "italic"))
        self.score_label.grid(row=0, column=1)
        # creating a canvas to display the questions
        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # creating questions to display
        self.question_text = self.canvas.create_text(150, 125, width=280, text="hello",
                                                     font=("Bahnschrift", 20, "italic"))
        # creating buttons true/false
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.btn_true = Button(image=true_img, highlightthickness=0, bd=0, command=self.true_pressed)
        self.btn_true.grid(row=2, column=0)
        self.btn_false = Button(image=false_img, highlightthickness=0, bd=0, command=self.false_pressed)
        self.btn_false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
