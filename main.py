import requests
import json
from tkinter import *
import datetime
from PIL import ImageTk, Image

# necessary details
root = Tk()
root.title("Weather App")
root.geometry("450x700")
root['background'] = "white"

api_key = "2248c6e6bc819fbdd57dd2a9d9768ef6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A,'), bg='white', font=("bold", 15))
date.place(x=10, y=130)
month = Label(root, text=dt.strftime('%B %m'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

# Time
hour = Label(root, text=dt.strftime('%I : %M %p'),
             bg='white', font=("bold", 15))
hour.place(x=10, y=160)

# City Search
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W + E + N + S)


def city_name():
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_entry.get() + "&units=metric&appid=" + api_key)

    api = json.loads(api_request.content)
    # store the value of "main"
    # key in variable y
    y = api["main"]

    # Temps
    current_temperature = y["temp"]
    current_temperature = (current_temperature * 9 / 5) + 32
    current_temperature = round(current_temperature, 2)

    tempmin = y['temp_min']
    tempmin = (tempmin * 9 / 5) + 32
    tempmin = round(tempmin, 2)

    tempmax = y['temp_max']
    tempmax = (tempmax * 9 / 5) + 32
    tempmax = round(tempmax, 2)

    # Humidity
    current_humidity = y["humidity"]
    current_humidity = str(current_humidity) + '%'

    # Country
    z = api['sys']
    country = z['country']
    citi = api['name']

    z = api["weather"]
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    lable_country.configure(text=country)
    lable_citi.configure(text=citi)
    lable_temp.configure(text=current_temperature)
    max_temp.configure(text=tempmax)
    min_temp.configure(text=tempmin)
    lable_humidity.configure(text=current_humidity)
    lable_weather_description.configure(text=weather_description)


# Search Bar and Button
city_nameButton = Button(root, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=5, stick=W + E + N + S)

# Country  Names and Coordinates
lable_citi = Label(root, text="...", width=0,
                   bg='white', font=("bold", 15))
lable_citi.place(x=10, y=100)

lable_country = Label(root, text="...", width=0,
                      bg='white', font=("bold", 15))
lable_country.place(x=135, y=100)

# Current Temperature
lable_temp = Label(root, text="...", width=0, bg='white',
                   font=("Helvetica", 110), fg='black')
lable_temp.place(x=18, y=220)

# Other temperature details
humi = Label(root, text="Humidity: ", width=0,
             bg='white', font=("bold", 15))
humi.place(x=3, y=400)

lable_humidity = Label(root, text="...", width=0,
                       bg='white', font=("bold", 15))
lable_humidity.place(x=107, y=400)

maxi = Label(root, text="Max. Temp.: ", width=0,
             bg='white', font=("bold", 15))
maxi.place(x=3, y=430)

max_temp = Label(root, text="...", width=0,
                 bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

mini = Label(root, text="Min. Temp.: ", width=0,
             bg='white', font=("bold", 15))
mini.place(x=3, y=460)

min_temp = Label(root, text="...", width=0,
                 bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

extra = Label(root, text="Description:", width=0,
             bg='white', font=("bold", 15))
extra.place(x=3, y=490)

lable_weather_description = Label(root, text="...", width=0,
                                  bg='white', font=("bold", 15))
lable_weather_description.place(x=128, y=490)

# Note
note = Label(root, text="All temperatures in Fahrenheit",
             bg='white', font=("italic", 10))
note.place(x=95, y=550)

root.mainloop()
