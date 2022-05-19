# Request description: Acquire Unexecuted Order List.
# Request type: GET
# Signature required: Yes
# Rate limit: 100/10s
# Request Header: authorization:"xxxx" (32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/pending
# Request parameter:    name 	    type 	required 	description
#                       market 	    String 	Yes 	    See <API invocation description·market>
#                       type 	    Integer No 	        Options: 0 or 1, 0 for sell order, 1 for buy order
#                       page 	    Integer Yes 	    Page, start from 1
#                       limit 	    Integer Yes 	    Amount per page(1-100)
#                       account_id 	Integer no 	        main account ID: 0,
#                                                       margin account ID: See < Inquire Margin Account Market Info >,
#                                                       future account ID: See < Inquire Future Account Market Info >
#
# Return value description: name 	        type 	description
#                           amount 	        String 	order count
#                           asset_fee 	    String 	asset fee
#                           avg_price 	    String 	average price
#                           create_time     Integer time when placing order
#                           deal_amount     String 	count
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
#                           status 	        String 	not_deal: unexecuted;
#                                                   part_deal: partly executed;
#                                                   done: executed;
#                           stock_fee 	    String 	stock fee
#                           taker_fee_rate 	String 	taker fee
#                           type 	        String 	sell: sell order; buy: buy order;
#                           client_id 	    String 	client_id: what you give


from tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Acquire Unexecuted Order List",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/order/pending",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],
                            ["type", int, False, [0, 1]],
                            ["page", int, True, []],
                            ["limit", int, True, []],
                            ["account_id", int, False, []]),
                 "params_as_data": False}

