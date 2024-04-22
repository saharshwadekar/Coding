import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = 'e438f96bdba074486f49ce76c79257f2'  
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.pack(pady=5)

        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.pack(pady=5)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack(pady=10)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_desc = data['weather'][0]['description'].capitalize()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            weather_info = f"Weather: {weather_desc}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
            self.weather_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", "Failed to fetch weather data.")

# Create GUI
root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
