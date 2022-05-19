# Request description: Acquire user deals.
# Request type: GET
# Signature required: Yes
# Request Header:authorization:"xxxx" (32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/user/deals
# Request parameter:    name 	    type 	required 	description
#                       market 	    String 	Yes 	    See <API invocation description·market>
#                       page 	    Integer	Yes 	    page, start from 1
#                       limit 	    Integer	Yes 	    amount per page(Max. 100)
#                       account_id 	Integer	No 	        main account ID: 0,
#                                                       margin account ID: See < Inquire Margin Account Market Info >,
#                                                       future account ID: See < Inquire Future Account Market Info >
#
# Return value description: name 	    type 	description
#                           amount 	    String 	executed amount
#                           create_time Integer executed time
#                           deal_money 	String 	executed value
#                           fee 	    String 	transaction fee
#                           fee_asset 	String 	transaction fee asset
#                           id 	        Integer executed id
#                           order_id 	Integer order no.
#                           price 	    String 	order price
#                           role 	    String 	order role
#                           type 	    String 	sell:sell; buy:buy


from Coinex_api_client.tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Acquire User Deals",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/order/user/deals",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],
                            ["page", int, True, []],
                            ["limit", int, True, []],
                            ["account_id", int, False, []]),
                 "params_as_data": False}

