import requests
import json

api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=bb496eb4-b857-467c-86de-efeb2f89f79f")

api = json.loads(api_request.content)

# Now I would be adding my own coin that I've invested
# coins = ["BTC", "ADA", "SOL"] Instead of list let's store it in a dictionary like json file
# coin name, amount no. of coins bought, price at which bought

print("<------------>")
print("<------------>")

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

total_pl = 0

# whenever I am hitting the run button I am sending a request so these req are counted in database and the daashboard
# I want info only of my portfolio
for i in range(0, 10):  # remember 5 is not included
    for coin in coins:
        # if the current coin is equal to my coin in list
        if api["data"][i]["symbol"] == coin["symbol"]:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * \
                api["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api["data"][i]["quote"]["USD"]["price"] - \
                coin["price_per_coin"]
            total_pl_coin = pl_percoin * coin["amount_owned"]

            total_pl = total_pl + total_pl_coin

            print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
            print(
                "Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("Number of Coin: ", coin["amount_owned"])
            print("Total Amount Paid: ", "${0:.2f}".format(total_paid))
            print("Current Value: ", "${0:.2f}".format(current_value))
            print("P/L Per coin: ", "${0:.2f}".format(pl_percoin))
            print("Total P/L with coin: ", "${0:.2f}".format(total_pl_coin))
            print("------------")

print("Total P/L for Portfolio: ", "${0:.2f}".format(total_pl))
