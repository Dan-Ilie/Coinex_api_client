# Request description: acquire multiple orders status in the same market, limit up to 100.
# Request type: GET
# Signature required: Yes
# Rate limit: 100/10s
# Request Header:authorization:"xxxx" (32-digit capital letters, see generating methos in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/status/batch
# Request parameter:    name 	    type 	required 	description
#                       batch_ids 	String 	Yes 	    multiple order nos string, comma+space separated
#                       market 	    String 	Yes 	    See <API invocation description·market>
#
# Return value description: name 	        type 	description
#                           amount 	        String 	order count
#                           asset_fee 	    String 	asset fee
#                           avg_price 	    String 	average price
#                           create_time 	Integer time when placing order
#                           deal_amount 	String 	count
#                           deal_fee 	    String 	transaction fee
#                           deal_money 	    String 	amount
#                           fee_asset 	    String 	fee asset
#                           fee_discount 	String 	fee discount
#                           finished_time 	Integer complete time
#                           id 	            Integer Order No.
#                           left 	        String 	left
#                           maker_fee_rate 	String 	maker fee
#                           money_fee 	    String 	money fee
#                           market 	        String 	See <API invocation description·market>
#                           order_type 	    String 	limit:limit order; market:market order;
#                           price 	        String 	order price
#                           status 	        String 	not_deal: unexecuted; part_deal: partly executed; done: executed;
#                           stock_fee 	    String 	stock fee
#                           taker_fee_rate 	String 	taker fee
#                           type 	        String 	sell: sell order; buy: buy order;
#                           client_id 	    String 	client_id: what you give


from Coinex_api_client.tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Acquire Multiple Orders Status",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/order/status/batch",
                 "authorization": True,
                 "params": (["batch_ids", str, True, []],
                            ["market", str, True, markets_list]),
                 "params_as_data": False}

