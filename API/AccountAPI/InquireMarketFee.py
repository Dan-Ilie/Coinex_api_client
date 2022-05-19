# Request description: Inquire market fee.
# Request type: GET
# Signature required: Yes
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/account/market/fee
# Request parameter:    name 	        type 	    required 	    description
#                       market 	        String 	    Yes 	        See<API invocation description·market>
#                       business_type 	String 	    No 	            use SPOT or PERPETUAL, default to SPOT
#
# Return value description:     name 	description
#                               taker 	taker fee
#                               maker 	maker fee


from tools.get_markets_list import markets_list


business_type_options = ["spot", "perpetual", "SPOT", "PERPETUAL"]

endpoint_info = {"endpoint": "Inquire Market Fee",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/account/market/fee",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],
                            ["business_type", str, False, business_type_options]),
                 "params_as_data": False}

