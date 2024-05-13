from tkinter import Tk, Label, StringVar, Canvas
from tkinter.ttk import Combobox
import time, math

win = Tk()
win.title("Digital Clock")
win.config(bg="white")

# size
win.geometry("500x400")
win.minsize(width=400, height=200)

# bg
win.config(bg="white")

# pinned
win.attributes("-topmost", 1)

def update_digital_clock():
    timeVar = time.strftime("%H:%M:%S %p")
    digital_clock.config(text=timeVar)
    digital_clock.after(200, update_digital_clock)

def update_analog_clock():
    analog_clock.delete("all") 
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

    # Draw clock face
    analog_clock.create_oval(2, 2, WIDTH, HEIGHT, outline="black", width=2)

    # Draw hour numbers
    for i in range(12):
        angle = i * math.pi/6 - math.pi/2
        x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
        y = HEIGHT/2 + 0.7 * WIDTH/2 * math.sin(angle)
        if i == 0:
            analog_clock.create_text(x, y-10, text=str(i+12), font=("Helvetica", 12))
        else:
            analog_clock.create_text(x, y, text=str(i), font=("Helvetica", 12))

    # Draw minute lines
    for i in range(60):
        angle = i * math.pi/30 - math.pi/2
        x1 = WIDTH/2 + 0.8 * WIDTH/2 * math.cos(angle)
        y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle)
        x2 = WIDTH/2 + 0.9 * WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)
        if i % 5 == 0:
            analog_clock.create_line(x1, y1, x2, y2, fill="black", width=3)
        else:
            analog_clock.create_line(x1, y1, x2, y2, fill="black", width=1)

    # Draw hour hand
    hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2
    hour_x = WIDTH/2 + 0.5 * WIDTH/2 * math.cos(hour_angle)
    hour_y = HEIGHT/2 + 0.5 * HEIGHT/2 * math.sin(hour_angle)
    analog_clock.create_line(WIDTH/2, HEIGHT/2, hour_x, hour_y, fill="black", width=6)

    # Draw minute hand
    minute_angle = (minute + second/60) * math.pi/30 - math.pi/2
    minute_x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(minute_angle)
    minute_y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(minute_angle)
    analog_clock.create_line(WIDTH/2, HEIGHT/2, minute_x, minute_y, fill="black", width=4)

    # Draw second hand
    second_angle = second * math.pi/30 - math.pi/2
    second_x = WIDTH/2 + 0.6 * WIDTH/2 * math.cos(second_angle)
    second_y = HEIGHT/2 + 0.6 * WIDTH/2 * math.sin(second_angle)
    analog_clock.create_line(WIDTH/2, HEIGHT/2, second_x, second_y, fill="red", width=2)

    analog_clock.after(1000, update_analog_clock)

def on_combobox_change(event):
    selected_option = variable.get()
    if selected_option == 'digital clock':
        analog_clock.pack_forget()
        digital_clock.pack()
        update_digital_clock()
    elif selected_option == 'analog clock':
        digital_clock.pack_forget()
        analog_clock.pack()
        update_analog_clock()

#choices
choices = ['digital clock', 'analog clock']
variable = StringVar(win)
variable.set('digital clock')

w = Combobox(win, values = choices)
w.pack()
w.bind("<<ComboboxSelected>>", on_combobox_change)

WIDTH = 400
HEIGHT = 400

digital_clock = Label(win, text="", font=("Helvetica", 48), fg="black", bg="white")
analog_clock = Canvas(win, width=WIDTH, height=HEIGHT, bg="white")

update_digital_clock()
update_analog_clock()

win.mainloop()