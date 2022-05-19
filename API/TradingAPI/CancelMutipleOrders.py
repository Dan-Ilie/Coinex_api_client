# Request description: cancel multiple orders in the same market, limit up to 100.
# Request type: DELETE
# Signature required: Yes
# Rate limit: 100/10s
# Request Header: authorization:"xxxx" (32-digit capital letters, see generating methos in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/pending/batch
# Request parameter:    name 	    type 	required 	description
#                       batch_ids 	String 	Yes 	    Unexecuted multiple order Nos string
#                       market 	    String 	Yes 	    See <API invocation description·market>
#                       account_id 	Integer No 	        main account ID: 0,
#                                                       margin account ID: See < Inquire Margin Account Market Info >,
#                                                       future account ID: See < Inquire Future Account Market Info >

# Return value description: name 	        type 	description
#                           amount 	        String 	order count
#                           avg_price 	    String 	average price
#                           create_time 	Integer time when placing order
#                           deal_amount 	String 	count
#                           deal_fee 	    String 	transaction fee
#                           deal_money 	    String 	executed value
#                           finished_time 	Integer complete time
#                           id 	            Integer Order No.
#                           maker_fee_rate 	String 	maker fee
#                           market 	        String 	See <API invocation description·market>
#                           order_type 	    String 	limit:limit order; market:market order;
#                           price 	        String 	order price
#                           status 	        String 	cancel: unexecuted; part_deal: partly executed; done: executed;
#                           taker_fee_rate 	String 	taker fee
#                           type 	        String 	sell: sell order; buy: buy order;
#                           client_id 	    String 	order client id


from tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Cancel Multiple Order",
                 "type": "delete",
                 "url": "https://api.coinex.com/v1/order/pending/batch",
                 "authorization": True,
                 "params": (["batch_ids", str, True, []],
                            ["market", str, True, markets_list],
                            ["account_id", int, False, []]),
                 "params_as_data": False}

