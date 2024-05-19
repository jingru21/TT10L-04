from tkinter import Tk , Label, Menu, Frame, Button
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
file_menu = Menu(menubar,tearoff=0)
file_menu.add_command(label='Close')
file_menu.add_separator()
file_menu.add_command(label='Exit',command=win.destroy)

menubar.add_cascade(label="File",menu=file_menu,underline=0)

# help menu
help_menu = Menu(menubar,tearoff=0)
help_menu.add_command(label='About...')
# help menu at menubar
menubar.add_cascade(label="Help",menu=help_menu,underline=0)

# add more selections from color theme
color_theme = Menu(file_menu, tearoff=0)
color_theme.add_command(label='Dark Theme', command=lambda: change_theme("dark"))
color_theme.add_command(label='Light Theme', command=lambda: change_theme("light"))
color_theme.add_command(label='Blue Theme', command=lambda: change_theme("blue"))
color_theme.add_command(label='Green Theme', command=lambda: change_theme("green"))
color_theme.add_command(label='Pink Theme', command=lambda: change_theme("pink"))


def change_theme(theme):
    if theme == "light":
        win.config(bg="white")
        update_calendar_colors("#FFB6C1", "#FF69B4", "#FF1493", "#FFB6C1", "#DC143C", "#FFB6C1", "#FFA07A")
    elif theme == "dark":
        win.config(bg="#1a1625")
        update_calendar_colors("#282828", "#3f3f3f", "#8b8b8b", "#46424f", "#717171", "#121212", "#5e5a66")
    elif theme == "blue":
        win.config(bg="#ADD8E6")
        update_calendar_colors("#ADD8E6", "#87CEEB", "#4682B4", "#87CEEB", "#4682B4", "#87CEEB", "#87CEEB")
    elif theme == "green":
        win.config(bg="#90EE90")
        update_calendar_colors("#90EE90", "#2E8B57", "#3CB371", "#90EE90", "#3CB371", "#90EE90", "#90EE90")
    elif theme == "pink":
        win.config(bg="#FFD1D7")
        update_calendar_colors("#FFB6C1", "#FF69B4", "#FF1493", "#FFB6C1", "#DC143C", "#FFB6C1", "#FFA07A")

def update_calendar_colors(bg, headersbg, selectbg, weekendbg, othermonthbg, headersfg, weekendfg):
    calendar.config(background=bg, 
                    headersbackground=headersbg, 
                    selectbackground=selectbg, 
                    weekendbackground=weekendbg, 
                    othermonthbackground=othermonthbg, 
                    headersforeground=headersfg, 
                    weekendforeground=weekendfg)

current_theme = "pink"

# frame for calendar and button
frame = Frame(win)
frame.pack(pady=20, padx=20, fill='both', expand=1)

#frame for button of theme color
theme_frame = Frame(frame)
theme_frame.pack(side='left', fill='y', padx=20, pady=20)

#button for theme
Button(theme_frame, text="Light Theme", command=lambda: change_theme("light")).pack(fill='x')
Button(theme_frame, text="Dark Theme", command=lambda: change_theme("dark")).pack(fill='x')
Button(theme_frame, text="Blue Theme", command=lambda: change_theme("blue")).pack(fill='x')
Button(theme_frame, text="Green Theme", command=lambda: change_theme("green")).pack(fill='x')
Button(theme_frame, text="Pink Theme", command=lambda: change_theme("pink")).pack(fill='x')


#calendar
def on_date_selected():
    selected_date = calendar.get_date()
    print("Selected date:", selected_date)

calendar = Calendar(
    frame,
    selectmode="day",
    date_pattern="yyyy-mm-dd",
    font="Arial 12",
    foreground="black",
    command=on_date_selected
)
calendar.pack(side='right', padx=20, pady=20, fill='both', expand=1)

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

change_theme(current_theme)

win.mainloop()
