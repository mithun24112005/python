# API CURRENCY CONVERTOR

import requests

API_KEY="fca_live_BOjs49xLOBUcTyKE2BeVT731EhheqFJjCKl5WRsq"
BASE_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES=["USD","CAD","AUD","CNY"]

def convert_currency(base):
    currencies=",".join(CURRENCIES)
    url=f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        responce=requests.get(url)
        data=responce.json()
        return data["data"]
    except :
        print("invalid currency")
        return None

while True:
    curr=input("enter the base currency (q for quit): ").upper()
    if curr=="Q":
        break
    data=convert_currency(curr)
    if not data:
        continue
    del data[curr]
    for ticker,value in data.items():
        print(f"{ticker}:{value}")
