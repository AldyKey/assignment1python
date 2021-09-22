import requests
import json

t = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h").text
t = json.loads(t)
p = input("Enter how many currencies I should show: ")
p = int(p)
for i in range(p):
    print(t[i]["id"])



