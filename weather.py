import requests

api = "4be5480c12825fe35ec3d2c75b600cf8"
city = input('City: ')
url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api}"
a = requests.get(url)
print(a.json().get("main"))