# importing requests and json
import requests, json
from csv import writer
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Tokyo"
API_KEY = "18066406cf9170857d927a4298cabdd1"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   data = response.json()
   main = data['main']
   min_temperature = main['temp_min']
   max_temperature = main['temp_max']
   temperature = main['temp']
   feels_like = main['feels_like']
   humidity = main['humidity']
   pressure = main['pressure']
   report = data['weather']


   print(f"{CITY:-^30}")
   print(f"Temperature: {min_temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")


Min_Temperature = str(min_temperature)
Max_Temperature = str(max_temperature)
Temperature = str(temperature)
Feels_like= str(feels_like)
Humidity = str(humidity)
Pressure = str(pressure)
datalist = [Min_Temperature,Max_Temperature,Temperature,Feels_like,Humidity,Pressure]
with open('tokyo weather new2.csv', 'a',newline='') as fd:
   csv_writer = writer(fd)
   csv_writer.writerow(datalist)

   fd.close()


print(data)
