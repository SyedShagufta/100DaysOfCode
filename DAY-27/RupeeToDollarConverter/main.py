import tkinter

window = tkinter.Tk()
window.title("Dollar to Rupees Converter.")
window.minsize(width=200, height=200)
window.config(padx=100, pady=100)


# logic to convert Rupees to dollars:
def convert():
    dollar = int(rupees_input.get()) * 83.24
    dollar_result_label["text"] = dollar


# Entry
rupees_input = tkinter.Entry(width=10)
rupees_input.grid(column=1, row=0)
# Labels
rupees_label = tkinter.Label(text="$ Dollars")
rupees_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

dollar_result_label = tkinter.Label(text="0")
dollar_result_label.grid(column=1, row=1)

dollar_label = tkinter.Label(text="Rupees")
dollar_label.grid(column=2, row=1)

# Button
calculate_button = tkinter.Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
