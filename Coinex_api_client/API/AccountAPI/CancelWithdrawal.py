# Request description: Cancel withdrawal.
# Request type: DELETE
# Signature required: Yes
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/balance/coin/withdraw
# Request parameter:    name 	            type 	    required 	description
#                       coin_withdraw_id 	Integer 	Yes 	    coin withdrawal id

# !!! NOTE! USE THIS TO DELETE A WITHDRAWAL ORDER. USE InquireWithdrawalList TO GET INFO FROM THE ORDER
# !!! InquireWithdrawalList USES SAME ADDRESS. Difference is that it uses GET, while this function uses DELETE


endpoint_info = {"endpoint": "Cancel Withdrawal",
                 "type": "delete",
                 "url": "https://api.coinex.com/v1/balance/coin/withdraw",
                 "authorization": True,
                 "params": (["coin_withdraw_id", int, True, []],),
                 "params_as_data": False}

