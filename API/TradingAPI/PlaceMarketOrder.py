# Request description:place market order.
# Request type: POST
# Signature required: Yes
# Request Header:authorization:"xxxx" (32-digit capital letters, see generating methods in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/market
# Request parameter:    name 	    type 	required 	description
#                       market 	    String 	Yes 	    See <API invocation description·market>
#                       type 	    String 	Yes 	    sell: Sell order; buy:Buy order;
#                       amount 	    String 	Yes     	Order amount(sell:table number,buy:table amount)
#                                                       when amount min. 0.001, accurate to 4 decimal places;
#                                                       when amount min. 0.01, accurate to 2 decimal places
#                       account_id 	Integer	no 	        margin account ID, See < Inquire Margin Account Market Info>
#                       client_id 	String 	no 	        client_id is the custom id of order. Currently, it only supports
#                                                       uppercase and lowercase letters, numbers, hyphens and underlines
#                                                       and it should be less than 32 bytes.
#                       source_id 	String 	no 	        user defines number and return
#
# Return value description: name 	        type 	description
#                           amount 	        String 	order count
#                           avg_price 	    String 	average price
#                           create_time 	Integer	time when placing order
#                           deal_amount 	String 	count
#                           deal_fee 	    String 	transaction fee
#                           deal_money 	    String 	amount
#                           fee_asset 	    String 	fee asset
#                           fee_discount 	String 	fee discount
#                           finished_time 	Integer	complete time
#                           id 	            Integer	Order No.
#                           left 	        String 	left amount
#                           maker_fee_rate 	String 	maker fee
#                           market 	        String 	See <API invocation description·market>
#                           order_type 	    String 	limit:limit order; market:market order;
#                           price 	        String 	order price
#                           status 	        String 	not_deal: unexecuted; part_deal: partly executed; done: executed;
#                           stock_fee 	    String 	stock fee
#                           taker_fee_rate 	String 	taker fee
#                           type 	        String 	sell: sell order; buy: buy order;
#                           client_id 	    String 	return what you give


from tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Place Market Order",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/order/market",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],
                            ["type", str, True, ['sell', 'buy']],
                            ["amount", str, True, []],
                            ["account_id", int, False, []],
                            ["client_id", str, False, []],
                            ["source_id", str, False, []]),
                 "params_as_data": True}

