import math
import winsound
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# --------------------------- Focus Window --------------------------- #
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


# ---------------------------- UI SETUP ------------------------------- #

# create a window for our project
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas design
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    start_btn.config(state="disabled")

    # if it is 1st/3rd/5th/7th rep then do work_sec
    if reps % 8 == 0:
        count_down(long_break_sec)
        text_label.config(text="BREAK", fg=RED)
        focus_window("on")
        # reset_timer()
        text_label.config(text="Congrats! 🥳🎉🌷 Reset to start again", font=(FONT_NAME, 15, "bold"))
        window.after_cancel(timer)
        # timer_text 00:00
        canvas.itemconfig(timer_text, text="00:00")

    # if it is 2/3/4/6 rep then short break and focus timer goes on at the time of breaks to alert
    elif reps % 2 == 0:
        count_down(short_break_sec)
        text_label.config(text="BREAK", fg=PINK)
        focus_window("on")
    else:
        count_down(work_sec)
        text_label.config(text="WORK", fg=GREEN)
        focus_window("on")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    time_in_minutes = math.floor(count / 60)
    time_in_seconds = count % 60
    if time_in_seconds < 10:
        time_in_seconds = f"0{time_in_seconds}"
    canvas.itemconfig(timer_text, text=f"{time_in_minutes}:{time_in_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_mark.config(text=marks)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # text_lable Timer
    text_label.config(text="Timer", bg=YELLOW)
    # reset check_marks
    global reps
    reps = 0
    tick_mark.config(text="")
    start_btn.config(state="normal")


# create a label
text_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)

text_label.grid(row=0, column=1)

# create start and stop buttons
start_btn = Button(text="Start", font=(FONT_NAME, 15, "bold"), width=5, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", font=(FONT_NAME, 15, "bold"), width=5, command=reset_timer)
reset_btn.grid(row=2, column=2)

# Tick mark label
tick_mark = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
tick_mark.grid(row=3, column=1)

window.mainloop()
