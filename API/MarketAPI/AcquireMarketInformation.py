# Request description: Acquire market detail information
# Request type: GET
# Signature required: No
# Request Url:https://api.coinex.com/v1/market/info
# Return value description:     name 	            type 	    description
#                               name 	            String 	    market name
#                               taker_fee_rate 	    String 	    taker fee
#                               maker_fee_rate 	    String 	    maker fee
#                               min_amount 	        String 	    Min. amount of transaction
#                               trading_name 	    String 	    tradiing coin type
#                               trading_decimal 	Integer 	decimal of tradiing coin
#                               pricing_name 	    String 	    pricing coin type
#                               pricing_decimal 	Integer 	decimal of pricing coin


endpoint_info = {"endpoint": "Acquire Market Detail Information",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/market/info",
                 "authorization": False,
                 "params": (),
                 "params_as_data": False}

