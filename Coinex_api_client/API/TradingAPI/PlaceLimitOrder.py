# Request description:place limit order.
# Request type: POST
# Signature required: Yes
# Rate limit: 100/10s
# Request Header: authorization:"xxxx" (32-digit capital letters, see generating methos in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/limit
# Request parameter:    name 	    type 	    required 	description
#                       market 	    String 	    Yes 	    See <API invocation description·market>
#                       type 	    String 	    Yes 	    sell: sell order; buy: buy order;
#                       amount 	    String 	    Yes 	    order amount, min. 0.001, accurate to 8 decimal places
#                       price 	    String 	    Yes 	    order amount, accurate to 8 decimal places
#                       source_id 	String 	    no 	        user defines number and return
#                       option 	    String 	    no 	        default value is NORMAL; order option, NORMAL: normal order,
#                                                           IOC: an Immediate or Cancel Order,
#                                                           FOK: Fill or kill Order,
#                                                           MAKER_ONLY: only maker order,
#                       account_id 	Integer 	no 	        main account ID: 0,
#                                                           margin account ID: see Inquire Margin Account Market Info
#                                                           future account ID: see Inquire Future Account Market Info
#                       client_id 	String 	    No 	        client_id is the custom id of order. Currently, it only
#                                                           supports uppercase and lowercase letters, numbers, hyphens
#                                                           and underlines, and it should be less than 32 bytes.
#                       hide 	    Boolean 	No 	        Whether to hide order, default to false

# Return value description:     name 	        type 	description
#                               amount 	        String 	order count
#                               asset_fee 	    String 	asset fee
#                               avg_price 	    String 	average price
#                               create_time 	Integer time when placing order
#                               deal_amount 	String 	count
#                               deal_fee 	    String 	transaction fee
#                               deal_money 	    String 	amount
#                               fee_asset 	    String 	fee asset
#                               fee_discount 	String 	fee discount
#                               finished_time 	Integer complete time
#                               id 	            Integer Order No.
#                               left 	        String 	left
#                               maker_fee_rate 	String 	maker fee
#                               money_fee 	    String 	money fee
#                               market 	        String 	See <API invocation description·market>
#                               order_type 	    String 	limit:limit order; market:market order;
#                               price 	        String 	order price
#                               status 	        String 	not_deal: unexecuted; part_deal: partly executed; done: executed
#                               stock_fee 	    String 	stock fee
#                               taker_fee_rate 	String 	taker fee
#                               type 	        String 	sell: sell order; buy: buy order;
#                               client_id 	    String 	client_id: what you give


from Coinex_api_client.tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Place Limit Order",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/order/limit",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],
                            ["type", str, True, ['sell', 'buy']],
                            ["amount", str, True, []],
                            ["price", str, True, []],
                            ["source_id", str, False, []],
                            ["option", str, False, ['NORMAL', 'IOC', 'FOK', 'MAKER_ONLY']],
                            ["account_id", int, False, []],
                            ["client_id", str, False, []],
                            ["hide", bool, False, [True, False]]),
                 "params_as_data": True}

