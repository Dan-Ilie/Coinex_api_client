# Request description: Inquire withdrawal list.
# Request type: GET
# Signature required: Yes
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/balance/coin/withdraw
# Request parameter:    name 	            type 	    required 	description
#                       coin_type 	        String 	    No 	        Coin type, e.g. BCH. Filter its withdrawal list
#                                                                   when the parameter is passed.
#                       coin_withdraw_id 	Integer 	No 	        Coin withdrawal id. Search its withdrawal record
#                                                                   when the parameter is passed.
#                       page 	            Integer 	No 	        Page, start from 1
#                       Limit 	            Integer 	No 	        Amount per page(1-100)
#
# Return value description:     name 	            description
#                               coin_withdraw_id 	coin withdrawal id
#                               create_time 	    create time
#                               amount 	            withdrawal amount
#                               actual_amount 	    actual withdrawal amount
#                               tx_id 	            tx id
#                               coin_address 	    withdrawal address
#                               tx_fee 	            tx fee
#                               confirmations 	    confirmations
#                               coin_type 	        coin type
#                               status 	            audit; pass; processing; confirming; not_pass; cancel; finish; fail;


from tools.get_coins_list import coins_list

endpoint_info = {"endpoint": "Inquire Withdrawal List",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/balance/coin/withdraw",
                 "authorization": True,
                 "params": (["coin_type", str, False, coins_list],
                            ["coin_withdraw_id", int, False, []],
                            ["page", int, False, []],
                            ["limit", int, False, []]),
                 "params_as_data": False}

