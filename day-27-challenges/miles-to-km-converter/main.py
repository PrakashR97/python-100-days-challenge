from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20,pady=20)

# Label
is_equal_label = Label(text="equal to")
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

kilometer_result_label = Label(text=" ")
kilometer_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=2)

entry = Entry(width=10)
entry.grid(column=1, row=0)


def mile_to_kilo():
    mile = entry.get()
    km = round(int(mile) * 1.60934)
    kilometer_result_label.config(text=km)


button = Button(text="Calculate", command=mile_to_kilo)
button.grid(column=1, row=2)

mainloop()
