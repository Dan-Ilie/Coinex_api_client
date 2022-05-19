# Request description: acquire asset config
# Request type: GET
# Signature required: No
# Request Url:https://api.coinex.com/v1/common/asset/config
# Request parameter:    name 	    type 	    required 	    description
#                       coin_type 	String 	    No 	            Coin type, e.g. BCH. If no coin_type is entered, the
#                                                               asset config of all the supported coins/tokens will be
#                                                               returned. If coin_type is provided, the asset config of
#                                                               the specific coin/token will be sent back instead.
#
# Return value description:         name 	                type 	    description
#                                   asset 	                String 	    coin type
#                                   chain 	                String 	    chain name
#                                   can_deposit 	        bool 	    coin type deposit status
#                                   can_withdraw 	        bool 	    coin type withdraw status
#                                   deposit_least_amount 	String 	    deposit least amount
#                                   withdraw_least_amount 	String 	    withdraw least amount
#                                   withdraw_tx_fee 	    String 	    withdraw tx fee


from tools.get_coins_list import coins_list


endpoint_info = {"endpoint": "Acquire Asset Config",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/common/asset/config",
                 "authorization": False,
                 "params": (["coin_type", str, False, coins_list],),
                 "params_as_data": False}

