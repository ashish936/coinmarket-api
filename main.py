import requests
import json

api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD&CMC_PRO_API_KEY=bb496eb4-b857-467c-86de-efeb2f89f79f")

api = json.loads(api_request.content)

print(api)
