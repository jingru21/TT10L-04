from tkinter import Tk, Label, Canvas, Button, Frame
import time
import math
import os

dirname = os.path.dirname(__file__)

win = Tk()
win.title("High-Class Clock")

# Size and minimum size
win.geometry("600x700")
win.minsize(width=500, height=600)

# Colors
bg_color = "#f0f0f0"  # Light grey background
fg_color = "#003366"  # Dark blue for text and accents
button_bg = "#004080"  # Darker blue for buttons
button_fg = "#ffffff"  # White text for buttons
clock_face_bg = "#ffffff"  # White for clock face
clock_outline = "#c0c0c0"  # Light grey for clock outline

win.config(bg=bg_color)

# Pinned
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
    analog_clock.create_oval(2, 2, WIDTH, HEIGHT, outline=clock_outline, width=2, fill=clock_face_bg)

    # Draw hour numbers
    for i in range(12):
        angle = i * math.pi / 6 - math.pi / 2
        x = WIDTH / 2 + 0.7 * WIDTH / 2 * math.cos(angle)
        y = HEIGHT / 2 + 0.7 * WIDTH / 2 * math.sin(angle)
        if i == 0:
            analog_clock.create_text(x, y - 10, text=str(i + 12), font=("Helvetica", 14, "bold"), fill=fg_color)
        else:
            analog_clock.create_text(x, y, text=str(i), font=("Helvetica", 14, "bold"), fill=fg_color)

    # Draw minute lines
    for i in range(60):
        angle = i * math.pi / 30 - math.pi / 2
        x1 = WIDTH / 2 + 0.8 * WIDTH / 2 * math.cos(angle)
        y1 = HEIGHT / 2 + 0.8 * HEIGHT / 2 * math.sin(angle)
        x2 = WIDTH / 2 + 0.9 * WIDTH / 2 * math.cos(angle)
        y2 = HEIGHT / 2 + 0.9 * HEIGHT / 2 * math.sin(angle)
        if i % 5 == 0:
            analog_clock.create_line(x1, y1, x2, y2, fill=fg_color, width=3)
        else:
            analog_clock.create_line(x1, y1, x2, y2, fill=fg_color, width=1)

    # Draw hour hand
    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    hour_x = WIDTH / 2 + 0.5 * WIDTH / 2 * math.cos(hour_angle)
    hour_y = HEIGHT / 2 + 0.5 * HEIGHT / 2 * math.sin(hour_angle)
    analog_clock.create_line(WIDTH / 2, HEIGHT / 2, hour_x, hour_y, fill=fg_color, width=6)

    # Draw minute hand
    minute_angle = (minute + second / 60) * math.pi / 30 - math.pi / 2
    minute_x = WIDTH / 2 + 0.7 * WIDTH / 2 * math.cos(minute_angle)
    minute_y = HEIGHT / 2 + 0.7 * HEIGHT / 2 * math.sin(minute_angle)
    analog_clock.create_line(WIDTH / 2, HEIGHT / 2, minute_x, minute_y, fill=fg_color, width=4)

    # Draw second hand
    second_angle = second * math.pi / 30 - math.pi / 2
    second_x = WIDTH / 2 + 0.6 * WIDTH / 2 * math.cos(second_angle)
    second_y = HEIGHT / 2 + 0.6 * WIDTH / 2 * math.sin(second_angle)
    analog_clock.create_line(WIDTH / 2, HEIGHT / 2, second_x, second_y, fill="#ff3333", width=2)

    analog_clock.after(1000, update_analog_clock)

WIDTH = 400
HEIGHT = 400

# Digital clock label
digital_clock = Label(win, text="", font=("Helvetica", 48, "bold"), fg=fg_color, bg=bg_color)
digital_clock.pack(pady=(20, 10))

# Analog clock canvas
analog_clock = Canvas(win, width=WIDTH, height=HEIGHT, bg=bg_color, highlightthickness=0)
analog_clock.pack()

update_digital_clock()
update_analog_clock()

def open_worldclock():
    worldclock_path = os.path.join(dirname, 'worldclock.py')
    os.system(f'python "{worldclock_path}"')

# Buttons frame
button_frame = Frame(win, bg=bg_color)
button_frame.pack(pady=20)

# CLOCK button
button_clock = Button(button_frame, text="CLOCK", width=15, height=2, bg=button_bg, fg=button_fg, font=("Helvetica", 12, "bold"))
button_clock.grid(row=0, column=0, padx=10)

# WORLD CLOCK button
button_world_clock = Button(button_frame, text="WORLD CLOCK", command=open_worldclock, width=15, height=2, bg=button_bg, fg=button_fg, font=("Helvetica", 12, "bold"))
button_world_clock.grid(row=0, column=1, padx=10)

# BACK button
button_exit = Button(button_frame, text="BACK", command=win.destroy, width=15, height=2, bg=button_bg, fg=button_fg, font=("Helvetica", 12, "bold"))
button_exit.grid(row=0, column=2, padx=10)

win.mainloop()
blue and grey
button_exit=Button(text="BACK", command=win.destroy, width=55, height=4)
button_exit.place(x=900,y=580)


win.mainloop()
