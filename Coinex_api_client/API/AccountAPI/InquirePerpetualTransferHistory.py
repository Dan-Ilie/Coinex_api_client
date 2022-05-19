# Request description: Inquire Transfer History list.
# Request type: GET
# Signature required: Yes
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/contract/transfer/history
# Request parameter:    name 	        type 	    required 	description
#                       transfer_type 	String 	    No 	        choices is one of transfer_in or transfer_out.
#                       asset 	        String 	    No 	        Coin type, e.g. BCH. Filter its withdrawal list when
#                                                               the parameter is passed.
#                       start_time 	    String 	    No 	        YY-mm-dd hh:MM for query time start.
#                       end_time 	    String 	    No 	        YY-mm-dd hh:MM for query time end.
#                       page 	        Integer 	No 	        Page, start from 1
#                       Limit 	        Integer 	No 	        Amount per page(1-100)
#
# Return value description:     name 	        description
#                               amount 	        operate amount
#                               asset 	        operate asset
#                               transfer_type 	transfer_in or transfer_out
#                               created_at 	    timestamp of created


from Coinex_api_client.tools.get_coins_list import coins_list

endpoint_info = {"endpoint": "Inquire Perpetual Transfer History",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/contract/transfer/history",
                 "authorization": True,
                 "params": (["transfer_type", str, False, ["transfer_in", "transfer_out"]],
                            ["asset", str, False, coins_list],
                            ["start_time", str, False, []],
                            ["end_time", str, False, []],
                            ["page", int, False, []],
                            ["limit", int, False, []]),
                 "params_as_data": False}

