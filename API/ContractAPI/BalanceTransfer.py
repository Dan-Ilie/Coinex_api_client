# Request description: Balance Transfer between contract and spot account
# Request type: POST
# Signature required: YES
# Request Url:https://api.coinex.com/v1/contract/balance/transfer
# Request Header:authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
#
# Request parameter:    name 	        type 	required 	description
#                       transfer_side 	String 	Yes 	    in or out
#                       coin_type 	    String 	Yes 	    contract market type
#                       amount 	        String 	Yes 	    coin amount
#
# Return value description:


from tools.get_coins_list import coins_list


endpoint_info = {"endpoint": "Balance Transfer",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/contract/balance/transfer",
                 "authorization": True,
                 "params": (["transfer_side", str, True, ["in", "out"]],
                            ["coin_type", str, True, coins_list],
                            ["amount", [int, float], True, []],),
                 "params_as_data": False}

