from tkinter import Tk
from tkinter import Label
import time
import sys

dc = Tk()
dc.title("Digital Clock")
dc.config(bg="black")

def get_time():
    timeVar = time.strftime("%H:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

title = Label(dc, font=("Arial",35), text="clock", fg="white", bg="black")
title.pack(anchor='w')
clock = Label(dc, text="", font=("Helvetica",48), fg="white", bg="black")
clock.pack()

get_time()

dc.mainloop()