import APIKey_Store
import math
from tkinter import *

# exception handling for requests package not being downloaded
try:
    import requests
except ModuleNotFoundError:
    print("Requests module not installed or found")
    exit(0)

if __name__ == '__main__':

    # Calling to the OpenWeatherMap API to access data
    def call_to_api(url):
        response = requests.get(url)
        json_response = response.json()
        return json_response

    # Attaining geo data
    while True:
        city = str(input("Enter a city or enter 0 for exit: "))
        if city == "0":
            exit(0)

        API_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey_Store.api}"
        API_data = call_to_api(API_url)

        # Attaining weather data
        try:
            city_temperature = int(API_data['main']['temp'])
            if city_temperature is None:
                raise IndexError("City stats not found.")
            city_temperature = math.floor(city_temperature - 273.15)

            feels_like_temp = API_data['main']['feels_like']
            feels_like_temp = math.floor(feels_like_temp - 273.15)

        # exception handling for incorrect city name or API key
        except KeyError:
            print("Invalid city name or API Key.")
            exit(1)

        # UI of the temperature stats
        window = Tk()
        window.geometry("400x400")
        window.title(f"{city.capitalize()}'s Temperature")

        city_label = Label(window, text=f"{city.capitalize()} Stats", bg="light blue")
        city_label.config(font=("Comic Sans MS", 40))
        city_label.pack(side='top')

        empty_space = Label(window, text="", bg = "light blue")
        empty_space.config()
        empty_space.pack(side="top")

        temp_label = Label(window, text=f"Temperature: {city_temperature} Degrees Celsius", bg="light blue")
        temp_label.config(font=("Comic Sans MS", 20))
        temp_label.pack(side="top")

        feels_like = Label(window, text=f"Feels Like: {city_temperature} Degrees Celsius", bg="light blue")
        feels_like.config(font=("Comic Sans MS", 20))
        feels_like.pack(side="top")

        window.configure(bg="light blue")
        window.mainloop()
