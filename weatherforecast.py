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
win.attributes("-topmost", 1)

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
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=27d637bf8af0772aa37a30a5702df3ae"

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
search_image = PhotoImage(file=r"image_weather\search.png")
myimage=Label(image=search_image)
myimage.place(x=10,y=20)

textfield=tk.Entry(win,font=("Arial",25,"bold"),justify="center",width=17,bg="#404040",border=0,fg="white")
textfield.place(x=80,y=40)
textfield.focus()

search_icon=PhotoImage(file=r"image_weather\search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0, cursor="hand2",bg="#404040",border=0, activebackground="#404040", command=getweather)
myimage_icon.place(x=390,y=34)

#logo
logo_image=PhotoImage(file=r"image_weather\logo.png")
logo=Label(image=logo_image)
logo.place(x=10,y=100)

#button box
frame_image=PhotoImage(file=r"image_weather\box.png")
frame=Label(image=frame_image)
frame.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(win,font=("arial",15,"bold"))
name.place(x=250,y=150)
clock=Label(win,font=("Helvetica",20))
clock.place(x=250,y=100)

#label
label1=Label(win,text="WIND",font=("Helvetica",10,"bold"),bg="#404040",fg="white")
label1.place(x=40,y=575)

label1=Label(win,text="HUMID",font=("Helvetica",10,"bold"),bg="#404040",fg="white")
label1.place(x=140,y=575)

label1=Label(win,text="INFO",font=("Helvetica",10,"bold"),bg="#404040",fg="white")
label1.place(x=220,y=575)

label1=Label(win,text="FORCE",font=("Helvetica",10,"bold"),bg="#404040",fg="white")
label1.place(x=350,y=575)

t = Label(win, font=("arial", 70, "bold"), fg="red")
t.place(x=10, y=350)
c = Label(win, font=("arial", 15, "bold"))
c.place(x=10, y=450)


w=Label(text="...",font=("arial",9,"bold"))
w.place(x=81,y=575)
h=Label(text="...",font=("arial",9,"bold"))
h.place(x=190,y=575)
d=Label(text="...",font=("arial",9,"bold"))
d.place(x=260,y=575)
p=Label(text="...",font=("arial",9,"bold"))
p.place(x=400,y=575)


win.mainloop()

#done