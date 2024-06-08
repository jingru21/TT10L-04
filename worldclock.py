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
      font = ("Times New Roman", 10)).grid(column = 0, row =0, padx = 10, pady = 25)

#Combobox
n = StringVar()
continents_cb = Combobox(win, width = 27, textvariable = n)

continents_cb['values'] = ('Africa',
                           'Asia',
                           'Australia',
                           'Europe',
                           'America')

continents_cb.grid(column=1, row=0, padx=10, pady=25)

def continents_changed(event):
    selected_option = continents_cb.get()
    if selected_option == 'Asia':
        update_asia()
    elif selected_option == 'Africa':
        update_africa()
        
def update_africa():
    home=pytz.timezone('Africa/Cairo')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%a %H:%M %p")
    clock.config(text=current_time)
    name.config(text="Egypt")

    home2=pytz.timezone('Africa/Casablanca')
    local_time=datetime.now(home2)
    current_time=local_time.strftime("%a %H:%M %p")
    clock2.config(text=current_time)
    name2.config(text="Morocco")

    home3=pytz.timezone('Africa/Gaborone')
    local_time=datetime.now(home3)
    current_time=local_time.strftime("%a %H:%M %p")
    clock3.config(text=current_time)
    name3.config(text="Botswana")

    home4=pytz.timezone('Africa/Algiers')
    local_time=datetime.now(home4)
    current_time=local_time.strftime("%a %H:%M %p")
    clock4.config(text=current_time)
    name4.config(text="Algeria")

def update_asia():
    home=pytz.timezone('Asia/Kuala_Lumpur')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%a %H:%M %p")
    clock.config(text=current_time)
    name.config(text="Malaysia")

    home2=pytz.timezone('Asia/Kolkata')
    local_time=datetime.now(home2)
    current_time=local_time.strftime("%a %H:%M %p")
    clock2.config(text=current_time)
    name2.config(text="India")

    home3=pytz.timezone('Asia/Singapore')
    local_time=datetime.now(home3)
    current_time=local_time.strftime("%a %H:%M %p")
    clock3.config(text=current_time)
    name3.config(text="Singapore")

    home4=pytz.timezone('Asia/Tokyo')
    local_time=datetime.now(home4)
    current_time=local_time.strftime("%a %H:%M %p")
    clock4.config(text=current_time)
    name4.config(text="Japan")

#first
f=Frame(win, bd=5)
f.place(x=200, y=118, width=300, height=150)

name=Label(f,font=("Helvetica", 30, "bold"))
name.place(x=50, y=10)

clock=Label(f, font=("Helvetica", 20))
clock.place(x=5, y=80)

#second
f2=Frame(win, bd=5)
f2.place(x=500, y=118, width=300, height=150)

name2=Label(f2,font=("Helvetica", 30, "bold"))
name2.place(x=30, y=10)

clock2=Label(f2, font=("Helvetica", 20))
clock2.place(x=5, y=80)

#third
f3=Frame(win, bd=5)
f3.place(x=200, y=300, width=300, height=150)

name3=Label(f3,font=("Helvetica", 30, "bold"))
name3.place(x=30, y=10)

clock3=Label(f3, font=("Helvetica", 20))
clock3.place(x=5, y=80)

#fourth
f4=Frame(win, bd=5)
f4.place(x=500, y=300, width=300, height=150)

name4=Label(f4,font=("Helvetica", 30, "bold"))
name4.place(x=30, y=10)

clock4=Label(f4, font=("Helvetica", 20))
clock4.place(x=5, y=80)

continents_cb.current()
continents_cb.bind("<<ComboboxSelected>>",continents_changed)

win.mainloop()