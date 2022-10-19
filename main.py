from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def getWeather():
    city = text_field.get()
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text = current_time)
    name.config(text="TIEMPO ACTUAL")

    #weather
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6ed3bbf40dfbaa6818f59e3ed08ad029"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp, "º"))
    c.config(text=(condition, "|", "Temperatura", "Actual", temp, "º"))

    v.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)


root = Tk()
root.title("Aplicación del clima")
root.geometry("900x500")
root.resizable(False, False)

# search box
search_image = PhotoImage(file="search.png")
my_image = Label(image=search_image)
my_image.place(x=20, y=20)

text_field = Entry(root, justify="center", width=21, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
text_field.place(x=50, y=40)
text_field.focus()

Search_icon = PhotoImage(file="search_icon.png")
my_image_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
my_image_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_my_image = Label(image=Frame_image)
frame_my_image.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Label
label_one = Label(root, text="Viento", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label_one.place(x=120, y=400)

label_two = Label(root, text="Humedo", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label_two.place(x=250, y=400)

label_three = Label(root, text="Despejado", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label_three.place(x=430, y=400)

label_four = Label(root, text="Presion", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label_four.place(x=650, y=400)

t = Label(font=("arial", 70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("arial",15,'bold'))
c.place(x=400,y=250)


v = Label(text="...", font=("arial", 20, "bold"),bg="#1ab5ef")
v.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"),bg="#1ab5ef")
h.place(x=250, y=430)
d = Label(text="...", font=("arial", 20, "bold"),bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(text="...", font=("arial", 20, "bold"),bg="#1ab5ef")
p.place(x=655, y=430)



#wind, humidity, descriptio, pressure
root.mainloop()