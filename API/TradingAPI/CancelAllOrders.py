# Request description: Cancel unexecuted order.
# Request type: DELETE
# Signature required: Yes
# Rate limit: 100/10s
# Request Header: authorization:"xxxx" (32-digit capital letters, see generating methos in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/order/pending
# Request parameter:    name 	    type 	required 	description
#                       account_id 	Integer Yes 	    main account ID: 0,
#                                                       margin account ID: See < Inquire Margin Account Market Info >,
#                                                       future account ID: See < Inquire Future Account Market Info >
#                       market 	    String 	Yes 	See <API invocation description·market>
#
# Return value description:


from tools.get_markets_list import markets_list


endpoint_info = {"endpoint": "Cancel All Orders",
                 "type": "delete",
                 "url": "https://api.coinex.com/v1/order/pending",
                 "authorization": True,
                 "params": (["account_id", int, True, []],
                            ["market", str, True, markets_list]),
                 "params_as_data": False}

