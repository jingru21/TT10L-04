from tkinter import Tk, Label, Button
import os

win = Tk()
win.title("Welcome to Almanac!")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

# pinned
win.attributes("-topmost", 1)

label = Label(win, text="Welcome to Almanac!!!", font=("Helvetica", 30))
label.pack(pady=20)

def open_calendar():
    os.system('python C:\\CSP1123\\GitProject\\TT10L-04\\mainInterface.py')

def open_clock():
    os.system('python C:\\CSP1123\\GitProject\\TT10L-04\\clock.py')

def open_weather():
    os.system('python C:\\CSP1123\GitProject\\TT10L-04\\weatherforecast.py')

import_button = [
    Button(win,text="Calendar", command=open_calendar),
    Button(win,text="Weather Forecast", command=open_weather),
    Button(win,text="Clock", command=open_clock),
    Button(win,text="Exit", command=win.destroy)
]


for button in import_button:
    button.pack(pady=2)

win.mainloop()