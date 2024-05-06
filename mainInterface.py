from tkinter import Tk , Label
from tkcalendar import Calendar

win = Tk()
win.title("Almanac")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

# icon
win.iconbitmap("C:\CSP1123\GitProject\TT10L-04\calendar.ico")

# bg
win.config(bg="skyblue")

# pinned
win.attributes("-topmost", 1)

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
calendar.pack(padx=10, pady=10)

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
