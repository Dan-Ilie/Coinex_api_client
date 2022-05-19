# Request description:  Inquire account asset constructure.
#                       When the total assets (available + frozen) of a coin are 0, no coin data return.
# Request type: GET
# Signature required: Yes
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/balance/info
# Return value description:     name 	    description
#                               frozen 	    frozen amount
#                               available 	available amount


endpoint_info = {"endpoint": "Inquire Account Info",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/balance/info",
                 "authorization": True,
                 "params": (),
                 "params_as_data": False}

