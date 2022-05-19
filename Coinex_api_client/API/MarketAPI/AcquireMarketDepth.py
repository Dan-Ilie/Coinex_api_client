# Request description: Acquire buy/sell statistics，return up to 50
# Request type: GET
# Signature required: No
# Request Url:https://api.coinex.com/v1/market/depth
# Request parameter:    name 	type 	    required 	    description
#                       market 	String 	    Yes 	        See<API invocation description·market>
#                       merge 	String 	    Yes 	        '0', '0.1', '0.01', '0.001', '0.0001', '0.00001',
#                                                           '0.000001', '0.0000001', '0.00000001
#                       limit 	Integer 	No(Default20) 	Return amount，range: 5/10/20/50
#
# Return value description:     name 	    type 	    description
#                               last 	    String 	    Last price
#                               time 	    Long 	    Updated time of Depth
#                               asks 	    Array 	    Seller depth
#                               asks[0][0] 	String 	    Order price
#                               asks[0][1] 	String 	    Order amount
#                               bids 	    Array 	    Buyer depth
#                               bids[0][0] 	String 	    Order price
#                               bids[0][1] 	String 	    Order amount


endpoint_info = {"endpoint": "Acquire Market Depth",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/market/depth",
                 "authorization": False,
                 "params": (["market", str, True, []],
                            ["merge", str, True, ['0', '0.1', '0.01', '0.001', '0.0001', '0.00001', '0.000001']],
                            ["limit", int, False, [5, 10, 20, 50]]),
                 "params_as_data": False}

