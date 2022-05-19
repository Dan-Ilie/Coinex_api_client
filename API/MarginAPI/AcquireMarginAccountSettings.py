# Request description: Get all information of the margin trading coin,
#                      including the general maximum loan amount, interest rate.
# Request type: GET
# Signature required: Yes
# Request Header:authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/margin/config
# Request parameter:    name 	type 	required 	description
#                       market 	String 	No 	        See <API invocation description·market>

# Return value description: name 	    type 	description
#                           amount 	    String 	maximum loan amount
#                           day_rate 	String 	daily interest rate
#                           leverage 	Integer maximum leverage
#                           market 	    String 	Market Name


from tools.get_markets_list import markets_list

endpoint_info = {"endpoint": "Acquire Margin Account Settings",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/margin/config",
                 "authorization": True,
                 "params": (["market", str, False, markets_list],),
                 "params_as_data": False}

