import requests
import win32com.client as wincom
import json
import time
from robo import speech

# def speech(text):
#     speak=wincom.Dispatch("SAPI.SpVoice")
#     speak.speak(text)
#     time.sleep(1)

city=input("enter the name of the city: ")
url=f"https://api.weatherapi.com/v1/current.json?key=5e4e6deb74724fad8a3142854241702&q={city}"
r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
text=f"the current weather in {city} is {w} degrees"
speech(text)


