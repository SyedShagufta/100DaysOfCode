import json
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0:
        messagebox.askokcancel("Oops.", message="Please don't leave any fields empty!")
    else:
        messagebox.askokcancel(f"Entered Data",
                               message=f"You entered the following data: \nWebsite name: {website}\nUsername/Email: {email}\nPassword: {password}")

        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        # with open("data.json", "r") as data_file:
        #     # Reading old data
        #     data = json.load(data_file)
        #     # Updating it
        #     data.update(new_data)
        #
        # with open("data.json", "w") as data_file:
        #     # writing new data
        #     json.dump(new_data, data_file, indent=4)
        #     username_entry.delete(0, END)
        #     password_entry.delete(0, END)


# --------------------------- Search --------------------------------- #

def find_password():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
        # print(data["facebook"]["email"])
    except FileNotFoundError:
        messagebox.askokcancel(title="Error", message="NO Data File Found!")
    else:
        website = website_entry.get().lower()
        if website in data:
            messagebox.askokcancel(title=website,
                                   message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")

        else:
            messagebox.askokcancel(title=website, message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager App 🗝️🔐")
window.config(padx=20, pady=20)

# create a canvas
canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# create entries, labels and buttons
website_text = Label(text="Website: ")
website_text.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky=EW)
website_entry.focus()

search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2)

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
username_entry.insert(0, "sweetyvox123@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=EW)

generate_password_btn = Button(text="Generate Password", command=password_generator)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
