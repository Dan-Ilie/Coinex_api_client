# Request description: Acquire k-line data for specified period, including latest 1000 datas
# Request type: GET
# Signature required: No
# Request Url:https://api.coinex.com/v1/market/kline?market=BCHBTC&type=1min
# Request parameter:    name 	type 	    required 	        description
#                       market 	String 	    Yes 	            See<API invocation description·market>
#                       limit 	Integer 	No(default 100) 	Less than or equal to 1000
#                       type 	String 	    Yes 	            1min:1min; 3min:3min; 5min:5min; 15min:15min;
#                                                               30min:30min; 1hour:1hour; 2hour:2hour; 4hour:4hour;
#                                                               6hour:6hour; 12hour:12hour; 1day:1day; 3day:3day;
#                                                               1week:1week;
#
# Return value description:         name 	    type 	    description
#                                   data[0][0] 	Integer 	Time
#                                   data[0][1] 	String 	    Opening price
#                                   data[0][2] 	String 	    Closing price
#                                   data[0][3] 	String 	    Highest price
#                                   data[0][4] 	String 	    Lowest price
#                                   data[0][5] 	String 	    Volume
#                                   data[0][6] 	String 	    Amount
#                                   data[0][7] 	String 	    Market


from Coinex_api_client.tools.get_markets_list import markets_list


type_list = ["1min", "3min", "5min", "15min", "30min", "1hour", "2hour", "4hour", "6hour", "12hour", "1day", "3day",
             "1week"]
endpoint_info = {"endpoint": "Acquire K-Line Data",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/market/kline",
                 "authorization": False,
                 "params": (["market", str, True, markets_list],
                            ["type", str, True, type_list],
                            ["limit", int, False, []]),
                 "params_as_data": False}

