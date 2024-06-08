from tkinter import Tk, Frame, Label, StringVar, Button
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

def refresh_window():
    selected_continent = continents_cb.get()
    if selected_continent == 'Asia':
        update_asia()
    elif selected_continent == 'Africa':
        update_africa()
    elif selected_continent == 'America':
        update_america()
    elif selected_continent == 'Europe':
        update_europe()
    elif selected_continent == 'Pacific':
        update_pacific()

#label
Label(win, text = "Select the Continents :",
      font = ("Times New Roman", 14)).grid(column = 0, row =0, padx = 10, pady = 25)

#Combobox
n = StringVar()
continents_cb = Combobox(win, width = 27, textvariable = n)

continents_cb['values'] = ('Africa',
                           'America',
                           'Asia',
                           'Europe',
                           'Pacific')

continents_cb.grid(column=1, row=0, padx=10, pady=25)

def continents_changed(event):
    selected_option = continents_cb.get()
    if selected_option == 'Asia':
        update_asia()
    elif selected_option == 'Africa':
        update_africa()
    elif selected_option == 'America':
        update_america()
    elif selected_option == 'Europe':
        update_europe()
    elif selected_option == 'Pacific':
        update_pacific()
        
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

def update_america():
    home = pytz.timezone('America/Los_Angeles')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M %p")
    clock.config(text=current_time)
    name.config(text="California")

    home2=pytz.timezone('America/Chicago')
    local_time=datetime.now(home2)
    current_time=local_time.strftime("%a %H:%M %p")
    clock2.config(text=current_time)
    name2.config(text="Chicago")

    home3=pytz.timezone('America/New_York')
    local_time=datetime.now(home3)
    current_time=local_time.strftime("%a %H:%M %p")
    clock3.config(text=current_time)
    name3.config(text="New York")

    home4=pytz.timezone('America/Toronto')
    local_time=datetime.now(home4)
    current_time=local_time.strftime("%a %H:%M %p")
    clock4.config(text=current_time)
    name4.config(text="Toronto")

def update_asia():
    home=pytz.timezone('Asia/Kuala_Lumpur')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%a %H:%M %p")
    clock.config(text=current_time)
    name.config(text="Malaysia")

    home2=pytz.timezone('Asia/Jakarta')
    local_time=datetime.now(home2)
    current_time=local_time.strftime("%a %H:%M %p")
    clock2.config(text=current_time)
    name2.config(text="Indonesia")

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

    home5=pytz.timezone('Asia/Ho_Chi_Minh')
    local_time=datetime.now(home5)
    current_time=local_time.strftime("%a %H:%M %p")
    clock5.config(text=current_time)
    name5.config(text="Vietnam")

    home6=pytz.timezone('Asia/Seoul')
    local_time=datetime.now(home6)
    current_time=local_time.strftime("%a %H:%M %p")
    clock6.config(text=current_time)
    name6.config(text="South Korea")

    home7=pytz.timezone('Asia/Bangkok')
    local_time=datetime.now(home7)
    current_time=local_time.strftime("%a %H:%M %p")
    clock7.config(text=current_time)
    name7.config(text="Thailand")

    home8=pytz.timezone('Asia/Dubai')
    local_time=datetime.now(home8)
    current_time=local_time.strftime("%a %H:%M %p")
    clock8.config(text=current_time)
    name8.config(text="United Arab Emirates")

def update_europe():
    home = pytz.timezone('Europe/London')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M %p")
    clock.config(text=current_time)
    name.config(text="London")

    home2=pytz.timezone('Europe/Paris')
    local_time=datetime.now(home2)
    current_time=local_time.strftime("%a %H:%M %p")
    clock2.config(text=current_time)
    name2.config(text="Paris")

    home3=pytz.timezone('Europe/Moscow')
    local_time=datetime.now(home3)
    current_time=local_time.strftime("%a %H:%M %p")
    clock3.config(text=current_time)
    name3.config(text="Moscow")

    home4=pytz.timezone('Europe/Amsterdam')
    local_time=datetime.now(home4)
    current_time=local_time.strftime("%a %H:%M %p")
    clock4.config(text=current_time)
    name4.config(text="Amsterdam")

def update_pacific():
    home = pytz.timezone('Pacific/Honolulu')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M %p")
    clock.config(text=current_time)
    name.config(text="Honolulu")

    home2=pytz.timezone('Pacific/Samoa')
    local_time=datetime.now(home2)
    current_time=local_time.strftime("%a %H:%M %p")
    clock2.config(text=current_time)
    name2.config(text="Samoa")

    home3=pytz.timezone('Pacific/Easter')
    local_time=datetime.now(home3)
    current_time=local_time.strftime("%a %H:%M %p")
    clock3.config(text=current_time)
    name3.config(text="Easter Island")

    home4=pytz.timezone('Pacific/Pago_Pago')
    local_time=datetime.now(home4)
    current_time=local_time.strftime("%a %H:%M %p")
    clock4.config(text=current_time)
    name4.config(text="Pago Pago")

#first
f=Frame(win, bd=5)
f.place(x=10, y=180, width=300, height=150)

name=Label(f,font=("Helvetica", 30, "bold"))
name.place(y=10)

clock=Label(f, font=("Helvetica", 20))
clock.place(x=5, y=80)

#second
f2=Frame(win, bd=5)
f2.place(x=300, y=180, width=300, height=150)

name2=Label(f2,font=("Helvetica", 30, "bold"))
name2.place(y=10)

clock2=Label(f2, font=("Helvetica", 20))
clock2.place(x=5, y=80)

#third
f3=Frame(win, bd=5)
f3.place(x=590, y=180, width=300, height=150)

name3=Label(f3,font=("Helvetica", 30, "bold"))
name3.place(y=10)

clock3=Label(f3, font=("Helvetica", 20))
clock3.place(x=5, y=80)

#fourth
f4=Frame(win, bd=5)
f4.place(x=880, y=180, width=300, height=150)

name4=Label(f4,font=("Helvetica", 30, "bold"))
name4.place(y=10)

clock4=Label(f4, font=("Helvetica", 20))
clock4.place(x=5, y=80)

#fifth
f5=Frame(win, bd=5)
f5.place(x=10, y=350, width=300, height=150)

name5=Label(f5,font=("Helvetica", 30, "bold"))
name5.place(y=10)

clock5=Label(f5, font=("Helvetica", 20))
clock5.place(x=10, y=80)

#sixth
f6=Frame(win, bd=5)
f6.place(x=300, y=350, width=300, height=150)

name6=Label(f6,font=("Helvetica", 30, "bold"))
name6.place(y=10)

clock6=Label(f6, font=("Helvetica", 20))
clock6.place(x=5, y=80)

#seventh
f7=Frame(win, bd=5)
f7.place(x=590, y=350, width=300, height=150)

name7=Label(f7,font=("Helvetica", 30, "bold"))
name7.place(y=10)

clock7=Label(f7, font=("Helvetica", 20))
clock7.place(x=5, y=80)

#eighth
f8=Frame(win, bd=5)
f8.place(x=880, y=350, width=300, height=150)

name8=Label(f8,font=("Helvetica", 30, "bold"))
name8.place(y=10)

clock8=Label(f8, font=("Helvetica", 20))
clock8.place(x=5, y=80)

refresh_label = Label(win, text="Click the button to refresh the window.", font=("Times New Roman", 12))
refresh_label.place(x=20, y=320)

refresh_button = Button(win, text="Refresh", command=refresh_window, font=("Times New Roman", 12))
refresh_button.place(x=300, y=320)

continents_cb.current()
continents_cb.bind("<<ComboboxSelected>>",continents_changed)

win.mainloop()