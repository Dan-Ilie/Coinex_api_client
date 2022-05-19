# NOT CHECKED YET!!!!


# Request description: transfer between main account and sub account.
# Request type: POST
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/sub_account/transfer
# Request parameter:    name 	            type 	    required 	description
#                       transfer_account 	String 	    Optional 	the sub account name
#                       transfer_side 	    String 	    Optional 	to post "in" or "out", in for deposit,
#                                                                   out for withdrawal
#                       coin_type 	        String 	    Yes 	    coin type
#                       amount 	            String 	    Yes 	    transfer amount
#
# If it is the main account using API, transfer_account (the sub account name) and transfer_side
# (in for deposit, out for withdrawal) are both required.
# If it is the sub account using the API, then neither of them is required, and the transfers are to the
# main account by default.


from Coinex_api_client.tools.get_coins_list import coins_list

endpoint_info = {"endpoint": "Transfer Between Main Account and Sub-Account",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/sub_account/transfer",
                 "authorization": True,
                 "params": (["transfer_account", str, False, []],
                            ["transfer_side", str, False, ["in", "out"]],
                            ["coin_type", str, True, coins_list],
                            ["amount", str, True, []]),
                 "params_as_data": False}

