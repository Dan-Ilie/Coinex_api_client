# Request description:place multiple limit orders in the same market, limit up to 100.
# Request type: POST
# Signature required: Yes
# Rate limit: 100/10s
# Request Header: authorization:"xxxx" (32-digit capital letters, see generating methos in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/limit/batch
# Request parameter:    name 	        type 	required 	description
#                       batch_orders 	String 	Yes 	    multiple orders json format string, add option parameter,
#                                                           order option, NORMAL: normal order,
#                                                           IOC: an Immediate or Cancel Order,
#                                                           FOK: Fill or kill Order,
#                                                           MAKER_ONLY: only maker order, default value is NORMAL
#                       market 	        String 	Yes 	    See <API invocation description·market>
#                       type 	        String 	Yes 	    sell: sell order; buy: buy order;
#                       amount 	        String 	Yes 	    order amount, min. 0.001, accurate to 8 decimal places
#                       price 	        String 	Yes 	    order amount, accurate to 8 decimal places
#                       source_id 	    String 	no 	        user defines number and return
#                       account_id 	    Integer	no 	        margin account ID/future account ID.
#                                                           If margin trade, See < Inquire Margin Account Market Info>.
#                                                           If future trade, See < Inquire Future Account Market Info>.

# Return value description:     name 	        type 	description
#                               amount 	        String 	order count
#                               avg_price 	    String 	average price
#                               create_time 	Integer time when placing order
#                               deal_amount 	String 	count
#                               deal_fee 	    String 	transaction fee
#                               deal_money 	    String 	amount
#                               finished_time 	Integer complete time
#                               id 	            Integer Order No.
#                               maker_fee_rate 	String 	maker fee
#                               market 	        String 	See <API invocation description·market>
#                               order_type 	    String 	limit:limit order; market:market order;
#                               price 	        String 	order price
#                               status 	        String 	not_deal: unexecuted; part_deal: partly executed; done: executed
#                               taker_fee_rate 	String 	taker fee
#                               type 	        String 	sell: sell order; buy: buy order;
#                               client_id 	    String 	client_id: return what you give;


from tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Place Multiple Limit Orders",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/order/limit/batch",
                 "authorization": True,
                 "params": (["batch_orders", str, True, []],
                            ["market", str, True, markets_list],
                            ["type", str, True, ['sell', 'buy']],
                            ["amount", str, True, []],
                            ["price", str, True, []],
                            ["source_id", str, False, []],
                            ["account_id", int, False, []]),
                 "params_as_data": True}

