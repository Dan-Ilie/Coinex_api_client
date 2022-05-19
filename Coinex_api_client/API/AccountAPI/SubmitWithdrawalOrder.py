# NOT CHECKED YET!!!!


# Request description: Submit a withdrawal order.
# Request type: POST
# Signature required: Yes
# Request Header: authorization:"xxxx"(32-digit capital letters, see generating method in <API invocation instruction>)
# Request Url:https://api.coinex.com/v1/balance/coin/withdraw
# Request parameter:    name 	                type 	    required 	description
#                       coin_type 	            String 	    Yes 	    coin_type
#                       smart_contract_name 	String 	    No 	        Multi-protocol USDT parameter: ERC20, TRC20,
#                                                                       CoinExChain (ERC20 is set by default for USDT);
#                                                                       No required for non-multi-protocol coin types.
#                       coin_address 	        String 	    Yes 	    Withdrawal address, which must be authorized
#                                                                       (Must add one record in Withdrawal Whitelist
#                                                                       (under Api management)). While withdrawing XMR
#                                                                       or XMC, use ":" to put “address” and
#                                                                       “payment_id” together and form "coin_address",
#                                                                       e.g. XXXX:yyyy. While withdrawing XRP, use ":"
#                                                                       to put “address” and “tag” together and form
#                                                                       "coin_address" if it has "tag". Inter-user
#                                                                       transfer supported via registered Mobile or
#                                                                       Email in CoinEx
#                       transfer_method 	    String 	    Yes 	    onchain -- Normal transfer local --
#                                                                       Inter-user transfer
#                       actual_amount 	        String 	    Yes 	    Withdrawal actual amount. Actual means the
#                                                                       actual amount of coins arrived in account after
#                                                                       deducting withdrawal fees. Check withdrawal
#                                                                       fees: https://www.coinex.com/fees
#
# Return value description:     name 	            description
#                               coin_withdraw_id 	coin withdrawal id
#                               create_time 	    create time
#                               amount 	            withdrawal amount
#                               actual_amount 	    actual amount
#                               tx_id 	            tx id
#                               coin_address 	    coin address
#                               tx_fee 	            tx fee
#                               confirmations 	    confirmations
#                               coin_type 	        coin type
#                               status 	            status of withdrawal


from Coinex_api_client.tools.get_coins_list import coins_list


endpoint_info = {"endpoint": "Submit Withdrawal Order",
                 "type": "post",
                 "url": "https://api.coinex.com/v1/balance/coin/withdraw",
                 "authorization": True,
                 "params": (["coin_type", str, True, coins_list],
                            ["smart_contract_name", str, False, ["ERC20", "TRC20", "CoinExChain"]],
                            ["coin_address", str, True, []],
                            ["transfer_method", str, True, ["onchain", "local"]],
                            ["actual_amount", str, True, []]),
                 "params_as_data": False}

