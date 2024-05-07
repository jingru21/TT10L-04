from tkinter import Tk, Label, StringVar
from tkinter.ttk import Combobox
import time

win = Tk()
win.title("Digital Clock")
win.config(bg="white")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

# bg
win.config(bg="white")

# pinned
win.attributes("-topmost", 1)

def get_time():
    timeVar = time.strftime("%H:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

title = Label(win, font=("Dina",35), text="clock", fg="black", bg="white")
title.pack(anchor='w')

#choices
choices = ['digital clock', 'analog clock']
variable = StringVar(win)
variable.set('digital clock')

w = Combobox(win, values = choices)
w.pack()

clock = Label(win, text="", font=("Helvetica",48), fg="black", bg="white")
clock.pack()


get_time()

win.mainloop()