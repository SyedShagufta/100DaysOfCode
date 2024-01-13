import random
import pandas
from tkinter import *

flip_timer = None
my_random_word = None
to_learn = None
BACKGROUND_COLOR = "#B1DDC6"
FONT_TEXT = "Ariel"
# ------------------------------------ Functionalities -------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    french_words = original_data.to_dict(orient="records")
else:
    french_words = data.to_dict(orient="records")


def next_card():
    global my_random_word, flip_timer
    window.after_cancel(flip_timer)
    my_random_word = random.choice(french_words)
    # o/p {'French': 'pendant', 'English': 'while'}
    # you can access like random_french_word['French'}
    # random_french_word = french_words[random.randint(0, 102)]["French"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=my_random_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global my_random_word
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, fill="White")
    canvas.itemconfig(word_text, fill="White")
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=my_random_word["English"])
def is_known():
    french_words.remove(my_random_word)
    # print(len(french_words))
    data = pandas.DataFrame(french_words)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()
# ---------------------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title("Flash Cards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(410, 270, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# title text
title_text = canvas.create_text(410, 150, text="Title", font=(FONT_TEXT, 40, "italic"))
# word text
word_text = canvas.create_text(410, 270, text="Word", font=(FONT_TEXT, 60, "bold"))
# create right and wrong buttons

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)

next_card()

window.mainloop()
