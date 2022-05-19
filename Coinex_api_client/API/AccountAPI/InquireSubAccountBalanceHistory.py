# Request description: Get Balance Transfer History Between Sub Account And Main Account(For Main Account Only)
# Request type: GET
# Signature required: YES
# Request Url:https://api.coinex.com/v1/sub_account/transfer/history
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request parameter:    name 	        type 	required 	description
#                       sub_user_name 	String 	Option 	    sub account username
#                       coin_type 	    String 	Option 	    coin type
#                       page 	        Integer Option 	    default 1
#                       limit 	        Integer Option 	    default 10, option(10, 100, 1000)
#
# Return value description:     name 	        type 	    description
#                               time 	        Integer 	unix timestamp (default order by type)
#                               coin_type 	    String 	    coin type
#                               amount 	        String 	    transfer amount
#                               transfer_from 	String 	    transfer from user name
#                               transfer_to 	String 	    transfer to user name


from Coinex_api_client.tools.get_coins_list import coins_list


endpoint_info = {"endpoint": "Inquire Sub-Account Balance History",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/sub_account/transfer/history",
                 "authorization": True,
                 "params": (["sub_user_name", str, False, []],
                            ["coin_type", str, False, coins_list],
                            ["page", int, False, []],
                            ["limit", int, False, []]),
                 "params_as_data": False}

