from tkinter import Tk , Label, Menu, Frame, Button
from tkcalendar import Calendar
import os

dirname = os.path.dirname(__file__)

win = Tk()
win.title("Almanac")

win.state('zoomed')
win.minsize(width=400, height=200)

# create a menubar
menubar = Menu(win)
win.config(menu=menubar)

# add more selections from color theme
color_theme = Menu(tearoff=0)
color_theme.add_command(label='Dark Theme', command=lambda: change_theme("dark"))
color_theme.add_command(label='Light Theme', command=lambda: change_theme("light"))
color_theme.add_command(label='Blue Theme', command=lambda: change_theme("blue"))
color_theme.add_command(label='Green Theme', command=lambda: change_theme("green"))
color_theme.add_command(label='Pink Theme', command=lambda: change_theme("pink"))


def change_theme(theme):
    if theme == "light":
        bg_color="white"
        button_bg = "#EDEDE9"
        button_fg = "black"
        update_calendar_colors("#F5EBE0", "#D5BDAF", "#E3D5CA", "#D6CCC2", "#E3D5CA", "black", "black")
        button_bg = "#FFB6C1"
        button_fg = "black"
        update_calendar_colors("#FFB6C1", "#FF69B4", "#FF1493", "#FFB6C1", "#DC143C", "#FFB6C1", "#FFA07A")
        button_bg = "#f7f5bc"
        button_fg = "black"
        update_calendar_colors("#ece75f", "#f7f5bc", "#f1ee8e", "#ece75f", "#e6cc00", "#e47200", "black")
    elif theme == "dark":
        bg_color="#1a1625"
        button_bg = "#282828"
        button_fg = "white"
        update_calendar_colors("#282828", "#3f3f3f", "#8b8b8b", "#717171", "#46424f", "#121212", "black")
    elif theme == "blue":
        bg_color="#ADD8E6"
        button_bg = "#87CEEB"
        button_fg = "black"
        update_calendar_colors("#61A5C2", "#2C7DA0", "#468FAF", "#A9D6E5", "#89C2D9", "black", "black")
    elif theme == "green":
        bg_color="#90EE90"
        button_bg = "#2E8B57"
        button_fg = "black"
        update_calendar_colors("#3A5A40", "#588157", "#90EE90", "#3CB371", "#344E41", "black", "black")
    elif theme == "pink":
        bg_color="#FFD1D7"
        button_bg = "#FFB6C1"
        button_fg = "black"
        update_calendar_colors("#FFB6C1", "#FF99AC", "#FF69B4", "#F7CAD0", "#FF477E", "black","black")
    
    win.config(bg=bg_color)
    frame.config(bg=bg_color) 
    theme_frame.config(bg=bg_color)
    for button in theme_buttons:
        button.config(bg=button_bg, fg=button_fg)

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
theme_buttons = [
 Button(theme_frame, text="Light Theme", command=lambda: change_theme("light")),
 Button(theme_frame, text="Dark Theme", command=lambda: change_theme("dark")),
 Button(theme_frame, text="Blue Theme", command=lambda: change_theme("blue")),
 Button(theme_frame, text="Green Theme", command=lambda: change_theme("green")),
 Button(theme_frame, text="Pink Theme", command=lambda: change_theme("pink")),
]

for button in theme_buttons:
    button.pack(fill='x', pady=2)
    
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

def open_todolist():
    todolist_path = os.path.join(dirname, 'todo.py')
    os.system(f'python "{todolist_path}"')

def open_reminder():
    reminder_path = os.path.join(dirname, 'reminder.py')
    os.system(f'python "{reminder_path}"')

exit_button = Button(win, text="Exit", command=win.destroy, bg="#F44336", fg="white", font=("Arial", 14, "bold"), padx=20, pady=10)
exit_button.pack(side="right", padx=10, pady=10)

todo_button = Button(win, text="To Do List", command=open_todolist, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), padx=20, pady=10)
todo_button.pack(side="right", padx=10, pady=10)

reminder_button = Button(win, text="Reminder", command=open_reminder, bg="#2196F3", fg="white", font=("Arial", 14, "bold"), padx=20, pady=10)
reminder_button.pack(side="right", padx=10, pady=10)

win.mainloop()

#done
