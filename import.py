from tkinter import Tk, Label, Button
import os

win = Tk()
win.title("Welcome to Almanac!")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

# pinned
win.attributes("-topmost", 1)

#bgcolor
win.config(bg="#797EF6")

label = Label(win, text="Welcome to Almanac!!!", font=("Comic Sans MS", 50), bg="#797EF6", fg="white")
label.pack(pady=20, side="top")

def open_calendar():
    os.system('python C:\\CSP1123\\GitProject\\TT10L-04\\mainInterface.py')

def open_clock():
    os.system('python C:\\CSP1123\\GitProject\\TT10L-04\\clock.py')

def open_weather():
    os.system('python C:\\CSP1123\GitProject\\TT10L-04\\weatherforecast.py')

import_button = [
    Button(win,text="Calendar", command=open_calendar,bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2),
    Button(win,text="Weather Forecast", command=open_weather,bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2),
    Button(win,text="Clock", command=open_clock, bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2),
    Button(win,text="Exit", command=win.destroy, bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2)
]


for button in import_button:
    button.pack(pady=2, anchor="center")

win.mainloop()