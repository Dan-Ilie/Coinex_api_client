# Request description: acquire currency rate
# Request type: GET
# Signature required: No
# Request Url:https://api.coinex.com/v1/common/currency/rate
# Request parameter: None
# Return value description:     name 	type 	description
#                               rate 	String 	currency rate

# !!!Note: it sends the currency rate for ONLY A FEW of the trading pairs currently on the platform


endpoint_info = {"endpoint": "Acquire Currency Rate",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/common/currency/rate",
                 "authorization": False,
                 "params": (),
                 "params_as_data": False}

