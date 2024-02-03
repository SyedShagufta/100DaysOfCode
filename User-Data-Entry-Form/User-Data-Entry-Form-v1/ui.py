from tkinter import *
from tkinter import ttk

def save_data():
    # data = {}
    first_name = first_name_entry.get()
    print(first_name)

    last_name = last_name_entry.get()
    print(last_name)

    title = title_combobox.get()
    print(title)

    age = age_spinbox.get()
    print(age)

    nationality = nationality_combobox.get()
    print(nationality)

    if registered.get() == 1:
        print("user is registered currently.")
    else:
        print("user not registered")

    completed_courses = completed_courses_spinbox.get()
    print(completed_courses)

    semesters = semesters_spinbox.get()
    print(semesters)

    if tc.get() == 1:
        print("User accepted terms and conditions..")
    else:
        print("user did not accept terms and conditions.")


    print("_______________________________________________________________________________\n")


# ------------------------------------------ UI --------------------------------------------------------------- #

# create a window
window = Tk()
window.title("Data Entry Form")
window.minsize(550, 400)
# create a frame
frame = Frame(window)
frame.pack()

# ----------------------------------------- USER INFORMATION FRAME ----------------------------------------- #

# create a label frame to display the user information
user_info_label = LabelFrame(frame, text="User Information")
user_info_label.grid(row=0, column=0, padx=20, pady=10)

# create first name label
first_name_label = Label(user_info_label, text="First Name")
first_name_label.grid(row=0, column=0)

# create first name entry box
first_name_entry = Entry(user_info_label)
first_name_entry.grid(row=1, column=0)

# create last name label
last_name_label = Label(user_info_label, text="Last Name")
last_name_label.grid(row=0, column=1)

# create last name entry
last_name_entry = Entry(user_info_label)
last_name_entry.grid(row=1, column=1)

# create a title label
title_label = Label(user_info_label, text="Title")
title_label.grid(row=0, column=2)

# create a combo box for title
title_values = ["Mr.", "Ms.", "Mrs."]
title_combobox = ttk.Combobox(user_info_label, values=title_values)
title_combobox.grid(row=1, column=2)

# create an age label
age_label = Label(user_info_label, text="Age")
age_label.grid(row=2, column=0)

# create a spin box for age
age_spinbox = ttk.Spinbox(user_info_label, from_=18, to=110)
age_spinbox.grid(row=3, column=0)

# create a nationality label
nationality_Label = Label(user_info_label, text="Nationality")
nationality_Label.grid(row=2, column=1)

# create a combo box for nationality
nationality_values = ["Australian", "American", "American", "Italian", "Chinese", "Asian"]
nationality_combobox = ttk.Combobox(user_info_label, values=nationality_values)
nationality_combobox.grid(row=3, column=1)

# let's add some padding to all the widgets in the user information frame
for widget in user_info_label.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# ----------------------- REGISTRATION STATUS FRAME ------------------------------------------- #

# create a label frame to display the Registration status
registration_label = LabelFrame(frame, padx=5)
registration_label.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# create a label registration status
registration_status_label = Label(registration_label, text="Registration Status")
registration_status_label.grid(row=0, column=0)

# create a check button
# if registered = 1 ( user is registered ) and if registered = 0 ( user is not registered )
registered = IntVar()
registered.set(0)
registration_check_button = Checkbutton(registration_label, text="Currently Registered", variable=registered, onvalue=1,
                                        offvalue=0)

registration_check_button.grid(row=1, column=0)

# completed courses - label
completed_courses_label = Label(registration_label, text="# Completed Courses")
completed_courses_label.grid(row=0, column=1)

# completed courses spinbox
completed_courses_spinbox = ttk.Spinbox(registration_label, from_=0, to=100)
completed_courses_spinbox.grid(row=1, column=1)

# semesters - label
semesters_label = Label(registration_label, text="Semesters")
semesters_label.grid(row=0, column=2)

# semesters spinbox
semesters_spinbox = ttk.Spinbox(registration_label, from_=0, to=100)
semesters_spinbox.grid(row=1, column=2)

# let's add some padding to all the widgets in the registration frame
for widget in registration_label.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# --------------------------- Terms & conditions ------------------------------------------------------- #
terms_and_conditions_label = LabelFrame(frame, text="Terms & Conditions")
terms_and_conditions_label.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# create a check box
tc = IntVar()
tc_checkbox = Checkbutton(terms_and_conditions_label, text="I accept terms and conditions.", variable=tc, onvalue=1,
                          offvalue=0)
tc_checkbox.grid(row=0, column=0)

# -------------------------------------------- Button ------------------------------------------------------------- #

save_data_button = Button(frame, text="Save Data", command=save_data)
save_data_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
