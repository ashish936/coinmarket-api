import requests
import json

api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=bb496eb4-b857-467c-86de-efeb2f89f79f")

api = json.loads(api_request.content)

# Now I would be adding my own coin that I've invested
# coins = ["BTC", "ADA", "SOL"] Instead of list let's store it in a dictionary like json file
coins = [
    {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 19100.59
    },
    {
        "symbol": "ADA",
        "amount_owned": 15,
        "price_per_coin": 0.99
    },
    {
        "symbol": "SOL",
        "amount_owned": 6,
        "price_per_coin": 31.46
    }
]


# whenever I am hitting the run button I am sending a request so these req are counted in database and the daashboard
# I want info only of my portfolio
for i in range(0, 10):  # remember 5 is not included
    for coin in coins:
        # if the current coin is equal to my coin in list
        if api["data"][i]["symbol"] == coin["symbol"]:
            print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
            print("{0: .2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("------------")


# coin name, amount no. of coins bought, price at which bought
