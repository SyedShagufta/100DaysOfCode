from functools import partial
from tkinter import *
from tkinter import ttk


THEME_COLOR = "#375362"





class SetupScreen:
    def __init__(self):
        self.parameters = None
        self.window = Tk()
        self.window.title("Setup Screen..")
        self.window.minsize(height=200, width=300)
        # create a frame
        self.frame = Frame(self.window)
        self.frame.pack()
        # create a heading label
        self.heading_label = LabelFrame(self.frame, text="Question Type")
        self.heading_label.grid(row=0, column=0, padx=20, pady=20)
        # create a labelframe
        self.questions_label = Label(self.heading_label, text="No Of Questions")
        self.questions_label.grid(row=0, column=0, padx=20, pady=10)
        # create a spin box for age
        self.question_spinbox = ttk.Spinbox(self.heading_label, from_=10, to=20)
        self.question_spinbox.grid(row=0, column=1, padx=20, pady=10)
        # category
        self.category_label = Label(self.heading_label, text="Category")
        self.category_label.grid(row=1, column=0, padx=20, pady=10)
        # create a combo box for category
        category_values = ["Any Category", "Sports", "History", "Vehicles"]
        self.category_combobox = ttk.Combobox(self.heading_label, values=category_values)
        self.category_combobox.grid(row=1, column=1, padx=20, pady=10)
        # level
        self.level_label = Label(self.heading_label, text="Difficulty")
        self.level_label.grid(row=2, column=0, padx=20, pady=10)
        # create a combo box for category
        level_values = ["Easy", "Medium", "Hard"]
        self.level_combobox = ttk.Combobox(self.heading_label, values=level_values)
        self.level_combobox.grid(row=2, column=1, padx=20, pady=10)
        self.save_data_button = Button(self.frame, text="Save Data", command=partial(get_parameters, self))
        self.save_data_button.grid(row=3, column=0, sticky="news", padx=10, pady=10)
    def get_parameters(self):
        questions = self.question_spinbox.get()
        category = self.category_combobox.get()
        difficulty = self.level_combobox.get()
        print(questions)
        print(category)
        print(difficulty)
        params = {
            "amount": questions,
            "type": "boolean",
            "category": category,
            "difficulty": difficulty,
        }
        return params

