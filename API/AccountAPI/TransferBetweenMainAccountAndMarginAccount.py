# NOT CHECKED YET!!!!


# Request description: transfer between main account and margin account.
# Request type: POST
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/margin/transfer
# Request parameter:    name 	        type 	    required 	description
#                       from_account 	Integer 	Yes 	    the remitting account ID, main account ID:0,
#                                                               margin account ID:
#                                                               See < Inquire Margin Account Market Info>
#                       to_account 	    Integer 	Yes 	    the remitting account ID, main account ID:0,
#                                                               margin account ID:
#                                                               See < Inquire Margin Account Market Info>
#                       coin_type 	    String 	    Yes 	    Coin type, e.g. BCH
#                       amount 	        String 	    Yes 	    transfer amount


from tools.get_coins_list import coins_list


endpoint_info = {"endpoint": "Transfer Between Main Account and Margin Account",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/margin/transfer",
                 "authorization": True,
                 "params": (["from_account", int, True, []],
                            ["to_account", int, True, []],
                            ["coin_type", str, True, coins_list],
                            ["amount", str, True, []]),
                 "params_as_data": False}

