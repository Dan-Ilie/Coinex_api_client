# Request description: Get loan history of the margin trading account.
# Request type: GET
# Signature required: Yes
# Request Header:authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/margin/loan/history
# Request parameter:    name 	    type 	required 	description
#                       market 	    String 	No 	        See<API invocation description·market>
#                       status 	    String 	No 	        status
#                       page 	    Integer	No 	        Page, start from 1
#                       limit 	    Integer	No 	        Amount per page(1-100)
#
# Return value description: name 	        type 	description
#                           loan_id 	    Integer	loan record ID
#                           create_time     Integer	create timestamp
#                           market 	        String 	See<API invocation description·market>
#                           coin_type 	    String 	coin token name
#                           loan_amount     String 	borrow amount
#                           unflat_amount 	String 	amount and interest need to repay
#                           expire_time 	Integer	expire timestamp
#                           is_renew 	    Boolean	false: close; true: open;
#                           day_rate 	    String 	daily interest rate
#                           status 	        String 	pass: in loan; burst: bankrupt; arrears: in debt; finish: paid off;


from Coinex_api_client.tools.get_markets_list import markets_list

endpoint_info = {"endpoint": "Acquire Loan List",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/margin/loan/history",
                 "authorization": True,
                 "params": (["market", str, False, markets_list],
                            ["status", str, False, ["pass", "burst", "arrears", "finish"]],
                            ["page", int, False, []],
                            ["limit", int, False, []]),
                 "params_as_data": False}

