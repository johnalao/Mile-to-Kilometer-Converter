from tkinter import *


def conversion():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    kilometer_results.config(text=f"{km}")


windows = Tk()
windows.title("Miles to Kilo Converter")
windows.config(padx=25, pady=25)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is Equal to ")
is_equal_label.grid(column=0, row=1)

kilometer_results = Label(text="0")
kilometer_results.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=conversion)
calculate_button.grid(column=1, row=2)


windows.mainloop()
