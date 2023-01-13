from tkinter import *


def miles_to_kms():
    miles = float(distance.get())
    kilometres = round(miles*1.609344, 2)
    converted_distance.config(text=kilometres)


# Window
window = Tk()
window.title("Miles to Kilometres")
window.minsize(width=150, height=100)

# Distance entry
distance = Entry(width=10)
distance.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Garamond", 18, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

# equal to label
is_equal = Label(text="is equal to", font=("Garamond", 18, "italic"))
is_equal.grid(column=0, row=1)
is_equal.config(padx=5, pady=5)

# converted distance
converted_distance = Label(text=0, font=("Garamond", 18, "italic"), fg='red')
converted_distance.grid(column=1, row=1)
converted_distance.config(padx=5, pady=5)

# Kilometres Label
miles_label = Label(text="Kms", font=("Garamond", 18, "normal"))
miles_label.grid(column=2, row=1)
miles_label.config(padx=5, pady=5)

# convert Button
convert = Button(text="Convert", command=miles_to_kms)
convert.grid(column=1, row=2)
convert.config(padx=5, pady=5)

window.mainloop()
