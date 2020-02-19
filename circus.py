import requests
  
url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando&units=imperial&appid=56711ed0a23dddf2661fd62d6da2ca44"
request = requests.get(url)

weather_json = request.json()
print(weather_json)
 
main_weather = weather_json['main']
 
temp = main_weather['temp']
 
print("The Circus's current temperature is ", temp)
