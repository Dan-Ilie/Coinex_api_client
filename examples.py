from Coinex_api_client.coinex import Coinex


# create an instance of Coinex API client
cnx = Coinex()

# Example1: send a simple request
a_request = cnx.acquire_asset_config("BTC")
print(a_request)

# Example2: configure with authentication details and send a request that requires authentication
cnx.config(access_id="this_is_my_access_id",
           secret_key="this_is_my_secret_key")
a_request = cnx.inquire_account_info()
print(a_request)
