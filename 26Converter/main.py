from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(250, 100)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    label3.config(text=f"{km:.2f}")

button = Button(text="Calculate")
button.grid(column=1, row=2)
button.config(command=calculate)




window.mainloop()