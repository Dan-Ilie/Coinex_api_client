# Request description: place stop limit order.
# Request type: POST
# Signature required: Yes
# Rate limit: 100/10s
# Request Header: authorization:"xxxx" (32-digit capital letters, see generating methos in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/stop/limit
# Request parameter:    name 	    type 	required 	description
#                       market 	    String 	Yes 	    See <API invocation description·market>
#                       type 	    String 	Yes 	    sell: sell order; buy: buy order;
#                       amount 	    String 	Yes 	    order amount, min. 0.001, accurate by market coin precision
#                       price 	    String 	Yes 	    order price, accurate by market coin precision
#                       stop_price 	String 	Yes 	    order stop price, accurate by market coin precision
#                       source_id 	String 	no 	        user defines number and return
#                       option 	    String 	no 	        order option, NORMAL: normal order,
#                                                       IOC: an Immediate or Cancel Order, default value is NORMAL
#                       account_id 	Integer	no 	        main account ID: 0,
#                                                       margin account ID: See < Inquire Margin Account Market Info >,
#                                                       future account ID: See < Inquire Future Account Market Info >
#                       client_id 	String 	No 	        client_id is the custom id of order. Currently, it only supports
#                                                       uppercase and lowercase letters, numbers, hyphens and underlines
#                                                       and it should be less than 32 bytes.
#                       hide 	    Boolean	no 	        whether to hide order, default to False
#
# Return value description: name 	type 	description
#                           status 	String 	success


from Coinex_api_client.tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Place Stop Limit Order",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/order/stop/limit",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],
                            ["type", str, True, ['sell', 'buy']],
                            ["amount", str, True, []],
                            ["price", str, True, []],
                            ["stop_price", str, True, []],
                            ["source_id", str, False, []],
                            ["option", str, False, ['NORMAL', 'IOC']],
                            ["account_id", int, False, []],
                            ["client_id", str, False, []],
                            ["hide", bool, False, [True, False]]),
                 "params_as_data": True}

