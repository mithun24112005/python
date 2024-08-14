# with api
import requests
api_key="cd6d57d0f7d3bcbff2b8591b2d29a5d5"
base_url="http://api.openweathermap.org/data/2.5/weather"

city=input("enter the city name:")
request_url=f"{base_url}?appid={api_key}&q={city}"
responce=requests.get(request_url)

if responce.status_code==200:
    data=responce.json()
    weather=data['weather'][0]['description']
    temparature=round(data["main"]["temp"]-273.15,2) #for celcious
    print("weather: ",weather)
    print("tempatature: ",temparature)
else:
    print("an error occured")

