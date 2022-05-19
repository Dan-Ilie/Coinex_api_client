# Request description: Acquire latest transaction data，return up to 1000
# Request type: GET
# Signature required: No
# Request Url:https://api.coinex.com/v1/market/deals?market=BCHBTC
# Request parameter:        name 	    type 	    required 	        description
#                           market 	    String 	    Yes 	            See<API invocation description·market>
#                           last_id 	Integer 	No 	                Transaction history id, send 0 to draw from
#                                                                       the latest record.
#                           limit 	    Integer 	No(default 100) 	Less than or equal to 1000
#
# Return value description:     name 	    type 	    description
#                               id 	        Integer 	Transaction No
#                               date 	    Integer 	Transaction time
#                               date_ms 	Integer 	Transaction time(ms)
#                               amount 	    String 	    Transaction amount
#                               price 	    String 	    Transaction price
#                               type 	    String 	    buy/sell;


from Coinex_api_client.tools.get_markets_list import markets_list

endpoint_info = {"endpoint": "Acquire Latest Transaction Data",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/market/deals",
                 "authorization": False,
                 "params": (["market", str, True, markets_list],
                            ["last_id", int, False, []],
                            ["limit", int, False, []]),
                 "params_as_data": False}

