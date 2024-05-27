from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz



win=Tk()
win.title("Weather App")
wingeometry=win.geometry("500x650+300+200")
win.resizable(False,False)

def getweather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)   
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9fa02c224b57c7507a3747e8fdb493fe"

        json_data=requests.get(api).json()
        print(json_data)
        condition=json_data['weather'][0]['main']
        description =json_data['weather'][0]['description']
        temp= int(json_data['main']['temp']-273.15)
        pressure =json_data['main']['pressure']
        humidity =json_data['main']['humidity']
        wind =json_data['wind']['speed']

        t.config(text=f"{temp}°C")  # Update temperature label
        c.config(text=f"{condition} | FEELS LIKE {temp}°C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=f"{description}")
        p.config(text=f"{pressure} hPa")
        
    except Exception as e:
        messagebox.showerror("Weather APP","Invalid Entry")  # Show error message box if any error occurs

#search box
search_image = PhotoImage(file=r"C:\spcalendar\TT10L-04\images_weather\search.png")
myimage=Label(image=search_image)
myimage.place(x=500,y=20)

textfield=tk.Entry(win,font=("Arial",25,"bold"),justify="center",width=17,bg="#404040",border=0,fg="white")
textfield.place(x=570,y=38)
textfield.focus()

search_icon=PhotoImage(file=r"C:\spcalendar\TT10L-04\images_weather\search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0, cursor="hand2",bg="#404040",border=0, activebackground="#404040", command=getweather)
myimage_icon.place(x=870,y=34)

#logo
logo_image=PhotoImage(file=r"C:\spcalendar\TT10L-04\images_weather\logo1.png")
logo=Label(image=logo_image)
logo.place(x=350,y=120)

#button box
button_image=PhotoImage(file=r"C:\spcalendar\TT10L-04\images_weather\box.png")
button=Label(image=button_image)
button.place(x=350,y=600)

#time
name=Label(win,font=("arial",25,"bold"))
name.place(x=900,y=240)
clock=Label(win,font=("arial",55,"bold"))
clock.place(x=900,y=150)

#label
label1=Label(win,text="WIND",font=("Helvetica",15,"bold"),bg="#404040",fg="white")
label1.place(x=420,y=625)

label1=Label(win,text="HUMID",font=("Helvetica",15,"bold"),bg="#404040",fg="white")
label1.place(x=600,y=625)

label1=Label(win,text="INFO",font=("Helvetica",15,"bold"),bg="#404040",fg="white")
label1.place(x=800,y=625)

label1=Label(win,text="FORCE",font=("Helvetica",15,"bold"),bg="#404040",fg="white")
label1.place(x=1000,y=625)


t = Label(win, font=("arial", 80, "bold"), fg="red")
t.place(x=900, y=300)
c = Label(win, font=("arial", 25, "bold"))
c.place(x=900, y=410)


w=Label(text="...",font=("arial",15,"bold"))
w.place(x=420,y=655)
h=Label(text="...",font=("arial",15,"bold"))
h.place(x=600,y=655)
d=Label(text="...",font=("arial",15,"bold"))
d.place(x=750,y=655)
p=Label(text="...",font=("arial",15,"bold"))
p.place(x=1000,y=655)


win.mainloop()