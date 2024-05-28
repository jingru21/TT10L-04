from tkinter import *
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from tkcalendar import Calendar

class WeatherApp:
    def __init__(self, master, go_back):
        self.master = master
        self.go_back = go_back
        self.setup_ui()

    def setup_ui(self):
        self.search_image = PhotoImage(file=r"C:\spcalendar\TT10L-04\images_weather\search.png")
        self.myimage = Label(self.master, image=self.search_image)
        self.myimage.place(x=500, y=20)

        self.textfield = Entry(self.master, font=("Arial", 25, "bold"), justify="center", width=17, bg="#404040", border=0, fg="white")
        self.textfield.place(x=570, y=38)
        self.textfield.focus()

        self.search_icon = PhotoImage(file=r"C:\spcalendar\TT10L-04\images_weather\search_icon.png")
        self.myimage_icon = Button(self.master, image=self.search_icon, borderwidth=0, cursor="hand2", bg="#404040", border=0, activebackground="#404040", command=self.getweather)
        self.myimage_icon.place(x=870, y=34)

        self.logo_image = PhotoImage(file=r"C:\spcalendar\TT10L-04\images_weather\logo1.png")
        self.logo = Label(self.master, image=self.logo_image)
        self.logo.place(x=350, y=120)

        self.button_image = PhotoImage(file=r"C:\spcalendar\TT10L-04\images_weather\box.png")
        self.button = Label(self.master, image=self.button_image)
        self.button.place(x=350, y=600)

        self.name = Label(self.master, font=("arial", 25, "bold"))
        self.name.place(x=900, y=240)
        self.clock = Label(self.master, font=("arial", 55, "bold"))
        self.clock.place(x=900, y=150)

        self.label1 = Label(self.master, text="WIND", font=("Helvetica", 15, "bold"), bg="#404040", fg="white")
        self.label1.place(x=420, y=625)
        self.label2 = Label(self.master, text="HUMID", font=("Helvetica", 15, "bold"), bg="#404040", fg="white")
        self.label2.place(x=600, y=625)
        self.label3 = Label(self.master, text="INFO", font=("Helvetica", 15, "bold"), bg="#404040", fg="white")
        self.label3.place(x=800, y=625)
        self.label4 = Label(self.master, text="FORCE", font=("Helvetica", 15, "bold"), bg="#404040", fg="white")
        self.label4.place(x=1000, y=625)

        self.t = Label(self.master, font=("arial", 80, "bold"), fg="red")
        self.t.place(x=900, y=300)
        self.c = Label(self.master, font=("arial", 25, "bold"))
        self.c.place(x=900, y=410)

        self.w = Label(self.master, text="...", font=("arial", 15, "bold"))
        self.w.place(x=420, y=655)
        self.h = Label(self.master, text="...", font=("arial", 15, "bold"))
        self.h.place(x=600, y=655)
        self.d = Label(self.master, text="...", font=("arial", 15, "bold"))
        self.d.place(x=750, y=655)
        self.p = Label(self.master, text="...", font=("arial", 15, "bold"))
        self.p.place(x=1000, y=655)

        self.back_button = ttk.Button(self.master, text="Back", command=self.go_back)
        self.back_button.place(x=50, y=50)

    def getweather(self):
        try:
            city = self.textfield.get()
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            self.clock.config(text=current_time)
            self.name.config(text="CURRENT WEATHER")

            api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9fa02c224b57c7507a3747e8fdb493fe"
            json_data = requests.get(api).json()

            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            self.t.config(text=f"{temp}°C")
            self.c.config(text=f"{condition} | FEELS LIKE {temp}°C")
            self.w.config(text=f"{wind} m/s")
            self.h.config(text=f"{humidity}%")
            self.d.config(text=f"{description}")
            self.p.config(text=f"{pressure} hPa")

        except Exception as e:
            messagebox.showerror("Weather APP", "Invalid Entry")

class CalendarApp:
    def __init__(self, master, go_back):
        self.master = master
        self.go_back = go_back
        self.setup_ui()

    def setup_ui(self):
        self.master.geometry("500x400")
        self.master.minsize(width=400, height=200)
        self.master.attributes("-topmost", 1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='Close')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.master.destroy)
        menubar.add_cascade(label="File", menu=file_menu, underline=0)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label='About...')
        menubar.add_cascade(label="Help", menu=help_menu, underline=0)

        color_theme = Menu(file_menu, tearoff=0)
        color_theme.add_command(label='Dark Theme', command=lambda: self.change_theme("dark"))
        color_theme.add_command(label='Light Theme', command=lambda: self.change_theme("light"))
        color_theme.add_command(label='Blue Theme', command=lambda: self.change_theme("blue"))
        color_theme.add_command(label='Green Theme', command=lambda: self.change_theme("green"))
        color_theme.add_command(label='Pink Theme', command=lambda: self.change_theme("pink"))
        file_menu.add_cascade(label='Color Theme', menu=color_theme)

        self.frame = Frame(self.master)
        self.frame.pack(pady=20, padx=20, fill='both', expand=1)

        self.theme_frame = Frame(self.frame)
        self.theme_frame.pack(side='left', fill='y', padx=20, pady=20)

        theme_buttons = [
            Button(self.theme_frame, text="Light Theme", command=lambda: self.change_theme("light")),
            Button(self.theme_frame, text="Dark Theme", command=lambda: self.change_theme("dark")),
            Button(self.theme_frame, text="Blue Theme", command=lambda: self.change_theme("blue")),
            Button(self.theme_frame, text="Green Theme", command=lambda: self.change_theme("green")),
            Button(self.theme_frame, text="Pink Theme", command=lambda: self.change_theme("pink")),
        ]

        for button in theme_buttons:
            button.pack(fill='x', pady=2)

        self.calendar = Calendar(
            self.frame,
            selectmode="day",
            date_pattern="yyyy-mm-dd",
            font="Arial 12",
            foreground="black",
            command=self.on_date_selected
        )
        self.calendar.pack(side='right', padx=20, pady=20, fill='both', expand=1)

        self.events = {
            "2024-01-01": "New Year",
            "2024-02-09": "Chinese New Year's Eve",
            "2024-02-10": "Chinese New Year",
            "2024-02-14": "Valentine's Day",
            "2024-03-11": "Ramadan",
            "2024-04-10": "Hari Raya",
            "2024-08-31": "Hari Merdeka",
            "2024-12-25": "Christmas",
            "2024-12-31": "New Year's Eve",
        }

        self.event_label = Label(self.master, text="", font=("Arial", 12), pady=10)
        self.event_label.pack()
        self.calendar.bind("<<CalendarSelected>>", self.on_specific_date_selected)

        self.change_theme("pink")

        self.back_button = ttk.Button(self.master, text="Back", command=self.go_back)
        self.back_button.pack()

    def change_theme(self, theme):
        if theme == "light":
            bg_color = "white"
            button_bg = "#f7f5bc"
            button_fg = "black"
            self.update_calendar_colors("#ece75f", "#f7f5bc", "#f1ee8e", "#ece75f", "#e6cc00", "#e47200", "black")
        elif theme == "dark":
            bg_color = "#1a1625"
            button_bg = "#282828"
            button_fg = "white"
            self.update_calendar_colors("#282828", "#3f3f3f", "#8b8b8b", "#717171", "#46424f", "#121212", "black")
        elif theme == "blue":
            bg_color = "#ADD8E6"
            button_bg = "#87CEEB"
            button_fg = "black"
            self.update_calendar_colors("#ADD8E6", "#87CEEB", "#4682B4", "#87CEEB", "#4682B4", "#87CEEB", "#87CEEB")
        elif theme == "green":
            bg_color = "#90EE90"
            button_bg = "#2E8B57"
            button_fg = "black"
            self.update_calendar_colors("#90EE90", "#2E8B57", "#3CB371", "#90EE90", "#3CB371", "#90EE90", "#90EE90")
        elif theme == "pink":
            bg_color = "#FFD1D7"
            button_bg = "#FFB6C1"
            button_fg = "black"
            self.update_calendar_colors("#FFB6C1", "#FF69B4", "#FF1493", "#FFB6C1", "#DC143C", "#FFB6C1", "#FFA07A")

        self.master.config(bg=bg_color)
        self.frame.config(bg=bg_color)
        self.theme_frame.config(bg=bg_color)
        for button in self.theme_frame.winfo_children():
            button.config(bg=button_bg, fg=button_fg)

    def update_calendar_colors(self, bg, headersbg, selectbg, weekendbg, othermonthbg, headersfg, weekendfg):
        self.calendar.config(
            background=bg,
            headersbackground=headersbg,
            selectbackground=selectbg,
            weekendbackground=weekendbg,
            othermonthbackground=othermonthbg,
            headersforeground=headersfg,
            weekendforeground=weekendfg
        )

    def on_date_selected(self):
        selected_date = self.calendar.get_date()
        print("Selected date:", selected_date)

    def on_specific_date_selected(self, event):
        date = self.calendar.get_date()
        if date in self.events:
            self.event_label.config(text=f"Event: {self.events[date]}", fg="#008000")
        else:
            self.event_label.config(text="No event for this date", fg="black")

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x800")
        self.login()

    def login(self):
        self.clear_window()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.place(x=50, y=50)
        self.reg_txt = ttk.Label(self.frame1, text='Login')
        self.reg_txt.place(x=50, y=50)
        self.register_btn = ttk.Button(self.frame1, text="Go to Register", command=self.register)
        self.register_btn.place(x=50, y=100)
        self.weather_btn = ttk.Button(self.frame1, text="Go to Weather App", command=self.weather_app)
        self.weather_btn.place(x=50, y=150)
        self.calendar_btn = ttk.Button(self.frame1, text="Go to Calendar App", command=self.calendar_app)
        self.calendar_btn.place(x=50, y=200)

    def register(self):
        self.clear_window()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.place(x=50, y=50)
        self.reg_txt2 = ttk.Label(self.frame2, text='Register')
        self.reg_txt2.place(x=50, y=50)
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.place(x=50, y=100)
        self.weather_btn = ttk.Button(self.frame2, text="Go to Weather App", command=self.weather_app)
        self.weather_btn.place(x=50, y=150)
        self.calendar_btn = ttk.Button(self.frame2, text="Go to Calendar App", command=self.calendar_app)
        self.calendar_btn.place(x=50, y=200)

    def weather_app(self):
        self.clear_window()
        WeatherApp(self.master, self.login)

    def calendar_app(self):
        self.clear_window()
        CalendarApp(self.master, self.login)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
