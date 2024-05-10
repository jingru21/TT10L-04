from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
rootgeometry=root.geometry("500x650+300+200")
root.resizable(False,False)

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
