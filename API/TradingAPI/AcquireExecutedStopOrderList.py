# Request description: Acquire Executed Stop Order List.
# Request type: GET
# Signature required: Yes
# Rate limit: 100/10s
# Request Header:authorization:"xxxx" (32-digit capital letters, see generating methods in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/stop/finished
# Request parameter:    name 	    type 	required 	description
#                       market 	    String 	Yes 	    See <API invocation description·market>
#                       page 	    Integer Yes 	    Page, start from 1
#                       limit 	    Integer Yes 	    Amount per page(1-100)
#                       account_id 	Integer No 	        main account ID: 0,
#                                                       margin account ID: See < Inquire Margin Account Market Info >,
#                                                       future account ID: See < Inquire Future Account Market Info >
#
# Return value description: name 	        type 	description
#                           amount 	        String 	order count
#                           order_id 	    Integer order no
#                           create_time     Integer time when placing order
#                           price 	        String 	order price
#                           stop_price 	    String 	stop price
#                           fee_asset 	    String 	fee asset
#                           fee_discount 	String 	fee discount
#                           market 	        String 	See <API invocation description·market>
#                           order_type 	    String 	limit:limit order; market:market order;
#                           type 	        String 	sell: sell order; buy: buy order;
#                           status 	        String 	not_deal: unexecuted; part_deal: partly executed; done: executed;


from tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Acquire Executed Stop Order List",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/order/stop/finished",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],
                            ["page", int, True, []],
                            ["limit", int, True, []],
                            ["account_id", int, False, []]),
                 "params_as_data": False}

