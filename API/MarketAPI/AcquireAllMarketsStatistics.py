# Request description: Acquire real-time market data
# Request type: GET
# Signature required: No
# Request Url: https://api.coinex.com/v1/market/ticker/all
#
# Return value description:     name 	        type 	description
#                               date 	        String 	server time when returning
#                               last 	        String 	latest price
#                               buy 	        String 	buy 1
#                               buy_amount 	    String 	buy 1 amount
#                               sell 	        String 	sell 1
#                               sell_amount 	String 	sell 1 amount
#                               open 	        String 	24H open price
#                               high 	        String 	24H highest price
#                               low 	        String 	24H lowest price
#                               vol 	        String 	24H volume


endpoint_info = {"endpoint": "Acquire All Markets Statistics",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/market/ticker/all",
                 "authorization": False,
                 "params": (),
                 "params_as_data": False}

