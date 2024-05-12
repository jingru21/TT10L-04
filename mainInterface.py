from tkinter import Tk , Label, Menu
from tkcalendar import Calendar

win = Tk()
win.title("Almanac")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

# pinned
win.attributes("-topmost", 1)

# create a menubar
menubar = Menu(win)
win.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='Close')
file_menu.add_separator()

# add more selections from color theme
color_theme = Menu(file_menu, tearoff=0)
color_theme.add_command(label='Dark Theme', command=lambda: change_theme("dark"))
color_theme.add_command(label='Light Theme', command=lambda: change_theme("light"))
color_theme.add_command(label='Blue Theme', command=lambda: change_theme("blue"))
color_theme.add_command(label='Green Theme', command=lambda: change_theme("green"))
color_theme.add_command(label='Pink Theme', command=lambda:change_theme("pink"))

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_cascade(
    label='Color Themes',
    menu=color_theme
)

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=win.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

def change_theme(theme):
    if theme == "light":
        win.config(bg="white")
    elif theme == "dark":
        win.config(bg="black")
    elif theme == "blue":
        win.config(bg="#ADD8E6")
    elif theme == "green":
        win.config(bg="#90EE90")
    elif theme == "pink":
        win.config(bg="#FFD1D7")

current_theme = "pink"

change_theme(current_theme)

#calendar
def on_date_selected():
    selected_date = calendar.get_date()
    print("Selected date: {selected_date}")

calendar = Calendar(
    win,
    selectmode="day",
    date_pattern="yyyy-mm-dd",
    font="Arial 12",
    foreground="black",
    background="#FFB6C1",
    headersbackground="#FF69B4",
    headersforeground="white",
    selectforeground="white",
    selectbackground="#FF1493",
    weekendforeground="#FF1493",
    weekendbackground="#FFB6C1",
    othermonthforeground="#DC143C",
    othermonthbackground="#FFB6C1",
    disabledforeground="#FFA07A",
    command=on_date_selected
)
calendar.pack(padx=100, pady=100)

#holiday
events = {
    "2024-01-01": "New Year",
    "2024-02-09":"Chinese New Year's Eve",
    "2024-02-10": "Chinese New Year",
    "2024-02-14": "Valentine's Day",
    "2024-03-11": "Ramadan",
    "2024-04-10": "Hari Raya",
    "2024-08-31": "Hari Merdeka",
    "2024-12-25": "Christmas",
    "2024-12-31": "New Year's Eve",
}
 
#date show 
def on_specific_date_selected(event):
 
    date = calendar.get_date()
    if date in events:
        event_label.config(text=f"Event: {events[date]}", fg="#008000")
    else:
        event_label.config(text=f"No event for this date", fg="black")
        pass
 
event_label = Label(win, text="", font=("Arial", 12), pady=10)
event_label.pack()
calendar.bind("<<CalendarSelected>>", on_specific_date_selected)

win.mainloop()
