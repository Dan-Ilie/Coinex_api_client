# Request description: Inquire deposit history
# Request type: GET
# Signature required: Yes
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/balance/coin/deposit
# Request parameter:    name 	    type 	    required 	description
#                       coin_type 	String 	    No 	        Coin type, e.g. BCH. Filter its withdrawal list when the
#                                                           parameter is passed.
#                       status 	    String 	    No 	        Status, options: PROCESSING/CONFIRMING/CANCELLED/FINISHED/
#                                                           TO_HOT/TOO_SMALL
#                       page 	    Integer 	No 	        Page, start from 1
#                       Limit 	    Integer 	No 	        Amount per page(1-100)
#
# Return value description:         name 	                description
#                                   actual_amount 	        actual deposit amount
#                                   actual_amount_display 	display of actual deposit amount
#                                   add_explorer 	        Depositor
#                                   amount 	                Amount
#                                   amount_display 	        Amount displayed
#                                   coin_address 	        Deposit add
#                                   coin_address_display 	Deposit add displayed
#                                   coin_deposit_id 	    Deposit ID
#                                   coin_type 	            Coin type
#                                   confirmations 	        confirmations
#                                   create_time 	        create time
#                                   explorer 	            explorer
#                                   remark 	                remark
#                                   status 	                processing，confirming，cancel，finish
#                                   status_display 	        Status displayed
#                                   transfer_method 	    transfer method
#                                   tx_id 	                tx id
#                                   tx_id_display 	        tx id display


from tools.get_coins_list import coins_list

status_options = ["PROCESSING", "CONFIRMING", "CANCELLED", "FINISHED", "TO_HOT", "TOO_SMALL"]

endpoint_info = {"endpoint": "inquire deposit list",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/balance/coin/deposit",
                 "authorization": True,
                 "params": (["coin_type", str, False, coins_list],
                            ["status", str, False, status_options],
                            ["page", int, False, []],
                            ["limit", int, False, []]),
                 "params_as_data": False}

