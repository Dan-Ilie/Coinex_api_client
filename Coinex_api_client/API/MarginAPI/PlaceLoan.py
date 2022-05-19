# Request description: Borrowing coins in a margin account.
# Request type: POST
# Signature required: Yes
# Request Header:authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/margin/loan
# Request parameter:    name 	    type 	required 	description
#                       market 	    String 	Yes 	    See<API invocation description·market>
#                       coin_type 	String 	Yes 	    Coin type, e.g. BCH
#                       amount 	    String 	Yes 	    borrow amount
#                       renew 	    Boolean No 	        whether renew order, missing is false
#
# Return value description: name 	    type 	    description
#                           loan_id 	Integer 	loan record ID


from Coinex_api_client.tools.get_markets_list import markets_list
from Coinex_api_client.tools.get_coins_list import coins_list

endpoint_info = {"endpoint": "Place Loan",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/margin/loan",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],
                            ["coin_type", str, True, coins_list],
                            ["amount", [int, float], True, []],
                            ["renew", bool, False, []]),
                 "params_as_data": False}

