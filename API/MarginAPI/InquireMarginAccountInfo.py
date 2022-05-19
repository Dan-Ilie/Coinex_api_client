# Request description: Inquire margin account asset constructure.
# Request type: GET
# Signature required: Yes
# Request Header:authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/margin/account
# Request parameter:    name 	type 	required 	description
#                       market 	String 	Yes 	    Market Name
#
# Return value description: name 	            type 	description
#                           account_id 	        Integer market account ID, See < Inquire Margin Account Market Info>
#                           leverage 	        Integer maximum leverage
#                           market_type 	    String 	<API invocation description·market>
#                           sell_asset_type     String 	sell coin name, equal "sell_type"
#                           buy_asset_type 	    String 	buy coin name, equal "buy_type"
#                           balance 	        Object 	balance
#                           frozen 	            Object 	amount frozen(not available)
#                           loan 	            Object 	amount loaned info
#                           interest 	        Object 	interest info
#                           can_transfer 	    Object 	available transfer amount
#                           warn_rate 	        String 	warn rate
#                           liquidation_price 	String 	burst price


from tools.get_markets_list import markets_list

endpoint_info = {"endpoint": "Inquire Margin Account Info",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/margin/account",
                 "authorization": True,
                 "params": (["market", str, True, markets_list],),
                 "params_as_data": False}

