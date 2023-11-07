from tkinter import *
def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    my_lable3.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=40, pady=40)

input = Entry(width=10)
input.grid(column=1, row=0)

my_lable1 = Label()
my_lable1.config(text="Miles")
my_lable1.grid(column=2, row=0)


my_lable2 = Label()
my_lable2.config(text="is equal to ")
my_lable2.grid(column=0, row=1)


my_lable3 = Label()
my_lable3.config(text=0)
my_lable3.grid(column=1, row=1)


my_lable4 = Label()
my_lable4.config(text="km")
my_lable4.grid(column=3, row=1)

cal = Button(text="Calculate",command=miles_to_km)
cal.grid(column=1, row=2)


window.mainloop()
