from tkinter import Tk, Frame, Label
from datetime import datetime
import pytz

win = Tk()
win.title("World Clock")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

# pinned
win.attributes("-topmost", 1)

def times():
    home=pytz.timezone('America/New_York')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%a %H:%M:%S")
    clock.config(text=current_time)
    name.config(text="New York")
    clock.after(1000, times)

f=Frame(win, bd=5)
f.place(x=10, y=118, width=220, height=150)

name=Label(f,font=("Helvetica", 30, "bold"))
name.place(x=50, y=10)

clock=Label(f, font=("Helvetica", 20))
clock.place(x=5, y=80)

times()

win.mainloop()