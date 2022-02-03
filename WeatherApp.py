from tkinter import *
import tkinter as tk
from tkinter import Button, ttk
import requests
import time



    

def getWeather():
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    summary = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    feels_like = int(json_data['main']['feels_like'] - 273.15)
    wind = json_data['wind']['speed']
    wind_gust = json_data['wind']['gust']
    

    final_data = "\n" + "Summary: " + str(summary) + "\n" \
    "\n" + "Current Temp: " + str(temp) + "°C" + "\n" + "\n" + "Wind Speed: " + \
        str(wind) + "km/h" + "\n" + "\n" + \
        "Feels Like Temp: " + str(feels_like) + "°C" + "\n" + \
        "\n"+ "Wind Gusts: " + str(wind_gust) + "°km/h" + "\n" 
            
    label.config(text=final_data, bg="White")
 

root = tk.Tk()
root.geometry("400x600")
root.title("My Weather App :)")

f = ("calibri", 15, "normal")
entry = ("calibri", 20, "italic")

textField = tk.Entry(root, justify='center', width=20, font=entry, bg="Beige")
textField.pack(pady=10)
textField.focus()

#def myClick():
 #   myLabel = tk.Label(root, final_data)
  #  myLabel.pack()


#textField.bind(myClick(), getWeather)

 

weatherButton = Button(text="Get Weather", padx=60, fg="White", bg="Black", command=getWeather)
weatherButton.pack()



label = tk.Label(root, font=f)
label.pack()
root.mainloop()
