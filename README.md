# Coinex API Client
Python 3 API client for Coinex trading platform. Using API spec from [Coinex API](https://github.com/coinexcom/coinex_exchange_api/wiki)


## Features
* Local parameter check
* Ability to choose how errors are handled
* Custom Exceptions
* Easy authenticated requests

## Note
Many functions from the Coinex API client require authentication data. You need to obtain an Access ID and secret key for your account using the steps mentioned [here](https://support.coinex.com/hc/en-us/articles/900004316323-What-is-API-and-how-to-Set-it-Up-) .

## Getting Started
### Installing Coinex API Client 
``` pip install git+https://github.com/Dan-Ilie/Coinex_api_client ```
### Importing Coinex API Client in your python project
``` from Coinex_api_client import coinex ```
### Initializing Coinex API Client
``` cnx = coinex.Coinex() ```

Alternatively you can also specify a few configs when initializing. These configs will be applied to all future requests to the API. Example:

```
cnx = coinex.Coinex(
            access_id = 'my access id that I got from coinex.com',
            secret_key = 'my secret key that I got from coinex.com'
            )
```

Configs can be modified like this:
```
cnx.config(
            access_id = 'a new access id'
            secret_key = 'a new secret key'
            )
```

And now, finally call a Coinex API endpoint like this:
```
response = cnx.acquire_asset_config("BTC")
print(response)
```

For a full list of endpoints check the wiki.
