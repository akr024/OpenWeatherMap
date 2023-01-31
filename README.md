# OpenWeatherMap:
OpenWeatherMap is a a Python program that is used to attain temperature statistics for any city using the OpenWeatherMap API and presents it with a clear user interface.

# Installation:
For this program to function appropriately, it relies on the following packages and libraries that must be installed using pip before running the program:
1. math
2. tkinter
3. requests
4. json

To download the project files, you can either download them directly using GitHub, copy/past the code, or clone them using the following HTTPS key:
https://github.com/akr024/OpenWeatherMap.git

Additionally, ensure that you have an API key from https://openweathermap.org/api that you input to the empty string 'api' in APIKey_Store.py since this program is utilising the openweathermap API to attain the temperature data and an API key is required to access this data.

Then, either press on the run button on any IDE of your choice, or run on the terminal using the following command:
python OpenWeatherMap.py

# Using the program:
After the program runs, you will have to input the name of a city for which you'd like to see the temperature of. Please input the name in English as OpenWeatherMap API contains cities primarily in English. After this, the program will run and open a tkinter interface where the actual temperature of the city and what feels like temperature of the city will be clearly visible.
