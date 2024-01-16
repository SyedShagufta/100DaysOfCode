from tkinter import *
import requests

MY_LAT = 15.338823
MY_LONG = 74.109970
RED = "#e7305b"
YELLOW = "#f7f5dd"
TEXT = ""
FONT_NAME = "Courier"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_data = (data["results"]["sunrise"]).split(":")
sunrise_hours = int(sunrise_data[0])+5
sunrise_minutes = int(sunrise_data[1])+5
sunrise = f"{sunrise_hours}:{sunrise_minutes} AM"

sunset_data = (data["results"]["sunset"]).split(":")
sunset_hours = int(sunset_data[0])+5
sunset_minutes = int(sunset_data[1])+5
sunset = f"{sunset_hours}:{sunset_minutes} PM"

def get_sunrise():
    global TEXT
    canvas.itemconfig(background, image=sunrise_img)
    text_label.config(text=sunrise)

def get_sunset():
    global TEXT
    canvas.itemconfig(background, image=sunset_img)
    text_label.config(text=sunset)


window = Tk()
window.title("Sunset and Sunrise Timings")
window.config()

canvas = Canvas(width=500, height=500)
background_img = PhotoImage(file="bck_img.png")
sunrise_img = PhotoImage(file="sunrise_img.png")
sunset_img = PhotoImage(file="sunset_img.png")
background = canvas.create_image(300, 300, image=background_img)
canvas.grid(row=0, column=0, columnspan=2)

text_label = Label(text="Welcome", font=(FONT_NAME, 20, "bold"))
text_label.grid(row=0, column=0)

sunrise_button = Button(text="Sunrise", font=(FONT_NAME, 15, "bold"), command=get_sunrise, width=10)
sunrise_button.grid(row=1, column=0)

sunset_button = Button(text="Sunset", font=(FONT_NAME, 15, "bold"), command=get_sunset, width=10)
sunset_button.grid(row=1, column=1)

window.mainloop()
