# Request type: PUT
# Need a signature：Yes
# Enquire deposit address: /balance/deposit/address/<string:coin_type>
# Request parameters notes:     Name 	                Type 	Required 	Description
#                               smart_contract_name 	Integer No 	        If there are multiple chains for a coin, it
#                                                                           needs to be specified.

# Currently, the multi-chain coin is USDT, smart_contract_name can be selected as Omni, ERC20, TRC20
# BTC, smart_contract_name can be selected as CoinExChain, BTC
# BCH, smart_contract_name can be selected as CoinExChain, BCH
# USDH, smart_contract_name can be selected as CoinExChain, SLP
# CET, smart_contract_name can be selected as CoinExChain, ERC20


from tools.get_coins_list import coins_list

endpoint_info = {"endpoint": "generate deposit address",
                 "type": "put",
                 "url": "https://api.coinex.com/v1/balance/deposit/address/",
                 "authorization": True,
                 "params": (["smart_contract_name", str, False, []],),
                 "dyn_url_param": (["coin_type", str, True, coins_list],),
                 "params_as_data": False}

