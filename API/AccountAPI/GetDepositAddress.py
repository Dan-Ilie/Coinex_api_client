# Request type: GET
# Need a signature：Yes
# Enquire deposit address: /balance/deposit/address/<string:coin_type>
# Request parameters:   Name 	                Type 	Required 	Description
#                       smart_contract_name 	Integer No 	        If there are multiple chains for a coin,
#                                                                   it needs to be specified.
#                       is_split 	            Integer No 	        Use Non-zero value to get a splited format

# Currently, the multi-chain coin is USDT, smart_contract_name can be selected as Omni, ERC20, TRC20
# BTC, smart_contract_name can be selected as CoinExChain, BTC
# BCH, smart_contract_name can be selected as CoinExChain, BCH
# USDH, smart_contract_name can be selected as CoinExChain, SLP
# CET, smart_contract_name can be selected as CoinExChain, ERC20


from tools.get_coins_list import coins_list


contract_names = ["Omni", "ERC20", "TRC20", "CoinExChain", "BTC", "BCH", "SLP", "ERC20"]

endpoint_info = {"endpoint": "Get Deposit Address",
                 "type": "get",
                 "url": "https://api.coinex.com/v1/balance/deposit/address/",
                 "authorization": True,
                 "params": (["smart_contract_name", str, False, contract_names],
                            ["is_split", int, False, [0, 1]]),
                 "dyn_url_param": (["coin_type", str, True, coins_list],),
                 "params_as_data": False}

