# gets the list of coins available on the Coinex platform

import requests

def get_coin_type_list():
    coin_list = []

    api_object = requests.get("https://api.coinex.com/v1/common/asset/config")
    values = api_object.json()['data'].values()
    for item in values:
        coin_list.append(item['asset'])
    return coin_list


def update_coins_list():
    globals()['coins_list'] = get_coin_type_list()


# use this variable to get the coins list
coins_list = get_coin_type_list()

