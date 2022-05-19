# gets the list of markets that are available on Coinex

import requests

def get_markets_list():
    api_object = requests.get("https://api.coinex.com/v1/market/list")
    market_list = api_object.json()['data']
    return market_list


def update_markets_list():
    globals()['markets_list'] = get_markets_list()


# use this variable to get the markets list
markets_list = get_markets_list()
