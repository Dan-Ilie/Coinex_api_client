# Request description: Acquire single market detail information
# Request type: GET
# Signature required: No
# Request Url:https://api.coinex.com/v1/market/detail
# Request parameter:        name 	type 	required 	description
#                           market 	String 	Yes 	    See<API invocation description·market>
#
# Return value description:         name 	            type 	    description
#                                   name 	            String 	    market name
#                                   taker_fee_rate 	    String 	    taker fee
#                                   maker_fee_rate 	    String 	    maker fee
#                                   min_amount 	        String 	    Min. amount of transaction
#                                   trading_name 	    String 	    trading coin type
#                                   trading_decimal 	Integer 	decimal of trading coin
#                                   pricing_name 	    String 	    pricing coin type
#                                   pricing_decimal 	Integer 	decimal of pricing coin


from Coinex_api_client.tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Acquire Single Market Information",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/market/detail",
                 "authorization": False,
                 "params": (["market", str, True, markets_list],),
                 "params_as_data": False}

