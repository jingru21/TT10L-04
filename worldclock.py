from tkinter import Tk, Frame, Label, StringVar
from datetime import datetime
from tkinter.ttk import Combobox
import pytz

win = Tk()
win.title("World Clock")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

# pinned
win.attributes("-topmost", 1)

#label
Label(win, text = "Select the Continents :",
      font = ("Times New Roman", 10)).grid(column = 0, row =5, padx = 10, pady = 25)

#Combobox
n = StringVar()
continents_cb = Combobox(win, width = 27, textvariable = n)

continents_cb['values'] = ('Africa',
                           'Antarctica',
                           'Asia',
                           'Australia',
                           'Europe',
                           'North America',
                           'South America')

continents_cb.grid(column=1, row=0, padx=10, pady=25)

def continents_changed(event):
    selected_option = continents_cb.get()
    if selected_option == 'Asia':
        update_asia()
        

def update_asia():
    home=pytz.timezone('Asia/Kuala_Lumpur')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%a %H:%M:%S %p")
    clock.config(text=current_time)
    name.config(text="Malaysia")
    clock.after(200, update_asia)

    home2=pytz.timezone('Asia/Kolkata')
    local_time=datetime.now(home2)
    current_time=local_time.strftime("%a %H:%M:%S %p")
    clock2.config(text=current_time)
    name2.config(text="India")
    clock2.after(200, update_asia)

    home3=pytz.timezone('Asia/Singapore')
    local_time=datetime.now(home3)
    current_time=local_time.strftime("%a %H:%M:%S %p")
    clock3.config(text=current_time)
    name3.config(text="Singapore")
    clock3.after(200, update_asia)

    home4=pytz.timezone('Asia/Tokyo')
    local_time=datetime.now(home4)
    current_time=local_time.strftime("%a %H:%M:%S %p")
    clock4.config(text=current_time)
    name4.config(text="Tokyo,Japan")
    clock4.after(200, update_asia)

#first
f=Frame(win, bd=5)
f.place(x=10, y=118, width=300, height=150)

name=Label(f,font=("Helvetica", 30, "bold"))
name.place(x=50, y=10)

clock=Label(f, font=("Helvetica", 20))
clock.place(x=5, y=80)

#second
f2=Frame(win, bd=5)
f2.place(x=300, y=118, width=300, height=150)

name2=Label(f2,font=("Helvetica", 30, "bold"))
name2.place(x=30, y=10)

clock2=Label(f2, font=("Helvetica", 20))
clock2.place(x=5, y=80)

#third
f3=Frame(win, bd=5)
f3.place(x=590, y=118, width=300, height=150)

name3=Label(f3,font=("Helvetica", 30, "bold"))
name3.place(x=30, y=10)

clock3=Label(f3, font=("Helvetica", 20))
clock3.place(x=5, y=80)

#fourth
f4=Frame(win, bd=5)
f4.place(x=10, y=300, width=300, height=150)

name4=Label(f4,font=("Helvetica", 30, "bold"))
name4.place(x=30, y=10)

clock4=Label(f4, font=("Helvetica", 20))
clock4.place(x=5, y=80)

continents_cb.current()
update_asia()

win.mainloop()