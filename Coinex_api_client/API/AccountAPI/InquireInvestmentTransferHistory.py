# Request description: Inquire Investment Transfer History list.
# Request type: GET
# Signature required: Yes
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/investment/transfer/history
# Request parameter:    name 	    type 	    required 	description
#                       op_type 	String 	    No 	        choices is one of in, out or interest.
#                       asset 	    String 	    No 	        Coin type, e.g. BCH. Filter its withdrawal list when the
#                                                           parameter is passed.
#                       start_time 	Integer 	No 	        Timestamp for query time start.
#                       end_time 	Integer 	No 	        Timestamp for query time end.
#                       page 	    Integer 	No 	        Page, start from 1
#                       Limit 	    Integer 	No 	        Amount per page(1-100)
#
# Return value description:     name 	    description
#                               amount 	    operate amount
#                               asset 	    operate asset
#                               opt_type
#                               created_at 	timestamp of created


from Coinex_api_client.tools.get_coins_list import coins_list


endpoint_info = {"endpoint": "Inquire Investment Transfer History",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/investment/transfer/history",
                 "authorization": True,
                 "params": (["op_type", str, False, ["in", "out", "interest"]],
                            ["asset", str, False, coins_list],
                            ["start_time", int, False, []],
                            ["end_time", int, False, []],
                            ["page", int, False, []],
                            ["limit", int, False, []]),
                 "params_as_data": False}

