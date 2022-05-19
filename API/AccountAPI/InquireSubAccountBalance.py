# Request description: Get Sub Account Balance (Main Account API key only)
# Request type: GET
# Signature required: YES
# Request Url:https://api.coinex.com/v1/sub_account/balance
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request parameter:    name 	        type 	    required 	description
#                       sub_user_name 	String 	    Option 	    Sub Account username
#                       coin_type 	    String 	    Option 	    coin type
#
# Return value description:     name 	    type 	description
#                               available 	String 	available amount
#                               frozen 	    String 	frozen amount


from tools.get_coins_list import coins_list

endpoint_info = {"endpoint": "Inquire Sub-Account Balance",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/sub_account/balance",
                 "authorization": True,
                 "params": (["sub_user_name", str, False, []],
                            ["coin_type", str, False, coins_list]),
                 "params_as_data": False}

