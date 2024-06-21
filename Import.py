from tkinter import Tk, Label, Button
import os
import sys

email = sys.argv[1] if len(sys.argv) > 1 else "Unknown User"

dirname = os.path.dirname(__file__)

win = Tk()
win.title("Welcome to Almanac!")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

#bgcolor
win.config(bg="#797EF6")

label = Label(win, text="Welcome to Almanac!!!", font=("Comic Sans MS", 50), bg="#797EF6", fg="white")
label.pack(pady=20, side="top")

def open_calendar():
    calendar_path = os.path.join(dirname, 'mainInterface.py')
    os.system(f'python "{calendar_path}"')

def open_clock():
    clock_path = os.path.join(dirname, 'clock.py')
    os.system(f'python "{clock_path}"')

def open_pomodoro():
    pomodoro_path = os.path.join(dirname, 'Pomodoro.py')
    os.system(f'python "{pomodoro_path}"')

def open_weather():
    weather_path = os.path.join(dirname, 'weatherforecast.py')
    os.system(f'python "{weather_path}"')

import_button = [
    Button(win,text="Calendar", command=open_calendar,bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2),
    Button(win,text="Weather Forecast", command=open_weather,bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2),
    Button(win,text="Pomodoro", command=open_pomodoro,bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2),
    Button(win,text="Clock", command=open_clock, bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2),
    Button(win,text="Exit", command=win.destroy, bg="lightblue", fg="black", font=("Comic Sans MS", 12),width=20, height=2)
]


for button in import_button:
    button.pack(pady=2, anchor="center")

win.mainloop()