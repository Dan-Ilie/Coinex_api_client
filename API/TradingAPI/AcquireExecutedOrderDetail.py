# Request description: Acquire Executed Order Detail.
# Request type: GET
# Signature required: Yes
# Request Header:authorization:"xxxx" (32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/deals
# Request parameter:    name 	    type 	required 	description
#                       id 	        Integer Yes 	    Order no.
#                       page 	    Integer Yes 	    page, start from 1
#                       limit 	    Integer Yes 	    amount per page(Max. 100)
#                       account_id 	Integer No 	        main account ID: 0,
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


endpoint_info = {"endpoint": "Acquire Executed Order Detail",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/order/deals",
                 "authorization": True,
                 "params": (["id", int, True, []],
                            ["page", int, True, []],
                            ["limit", int, True, []],
                            ["account_id", int, False, []]),
                 "params_as_data": False}

