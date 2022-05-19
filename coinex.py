from tools.errors import ArgumentTypeErr, ArgumentValueErr
from tools.apicall import APICall

from API.CommonAPI.AcquireAssetConfig import endpoint_info as get_asset_config
from API.CommonAPI.AcquireCurrencyRate import endpoint_info as get_currency_rate
from API.CommonAPI.AcquireSiteMaintainInfo import endpoint_info as get_site_maintain_info
from API.AccountAPI.AcquireCreditAccountInfo import endpoint_info as get_credit_account_info
from API.AccountAPI.CancelWithdrawal import endpoint_info as delete_withdrawal
from API.AccountAPI.GenerateDepositAddress import endpoint_info as put_deposit_address
from API.AccountAPI.GetDepositAddress import endpoint_info as get_deposit_addres
from API.AccountAPI.InquireAccountInfo import endpoint_info as get_account_info
from API.AccountAPI.InquireDepositList import endpoint_info as get_deposit_list
from API.AccountAPI.InquireInvestmentTransferHistory import endpoint_info as get_investment_transfer_history
from API.AccountAPI.InquireMarginAccountMarketInfo import endpoint_info as get_margin_account_market_info
from API.AccountAPI.InquireMarginTransferHistory import endpoint_info as get_margin_transfer_history
from API.AccountAPI.InquireMarketFee import endpoint_info as get_market_fee
from API.AccountAPI.InquirePerpetualTransferHistory import endpoint_info as get_perpetual_transfer_history
from API.AccountAPI.InquireSubAccountBalance import endpoint_info as get_subaccount_balance
from API.AccountAPI.InquireSubAccountBalanceHistory import endpoint_info as get_subaccount_balance_history
from API.AccountAPI.InquireWithdrawalList import endpoint_info as get_withdrawal_list
from API.AccountAPI.SubmitWithdrawalOrder import endpoint_info as post_withdrawal_order
from API.AccountAPI.TransferBetweenMainAccountAndMarginAccount import endpoint_info as post_transfer_main_margin
from API.AccountAPI.TransferBetweenMainAccountAndSubAccount import endpoint_info as post_transfer_main_sub
from API.ContractAPI.BalanceTransfer import endpoint_info as post_balance_transfer
from API.MarginAPI.AcquireLoanList import endpoint_info as get_loan_list
from API.MarginAPI.AcquireMarginAccountSettings import endpoint_info as get_margin_account_settings
from API.MarginAPI.InquireMarginAccountInfo import endpoint_info as get_margin_account_info
from API.MarginAPI.PlaceFlat import endpoint_info as post_flat
from API.MarginAPI.PlaceLoan import endpoint_info as post_loan
from API.MarketAPI.AcquireAMMMarketList import endpoint_info as get_amm_market_list
from API.MarketAPI.AcquireKLineData import endpoint_info as get_kline_data
from API.MarketAPI.AcquireLatestTransactionData import endpoint_info as get_latest_transaction_data
from API.MarketAPI.AcquireMarketDepth import endpoint_info as get_market_depth
from API.MarketAPI.AcquireSingleMarketInformation import endpoint_info as get_single_market_information
from API.MarketAPI.AcquireMarketInformation import endpoint_info as get_market_information
from API.MarketAPI.AcquireMarketList import endpoint_info as get_market_list
from API.MarketAPI.AcquireMarketStatistics import endpoint_info as get_market_statistics
from API.MarketAPI.AcquireAllMarketsStatistics import endpoint_info as get_all_markets_statistics
from API.TradingAPI.AcquireExecutedOrderDetail import endpoint_info as get_executed_order_detail
from API.TradingAPI.AcquireExecutedOrderList import endpoint_info as get_executed_order_list
from API.TradingAPI.AcquireExecutedStopOrderList import endpoint_info as get_executed_stop_order_list
from API.TradingAPI.AcquireMultipleOrdersStatus import endpoint_info as get_multiple_orders_status
from API.TradingAPI.AcquireOrderStatus import endpoint_info as get_order_status
from API.TradingAPI.AcquireUnexecutedOrderList import endpoint_info as get_unexecuted_order_list
from API.TradingAPI.AcquireUnexecutedStopOrderList import endpoint_info as get_unexecuted_stop_order_list
from API.TradingAPI.AcquireUserDeals import endpoint_info as get_user_deals
from API.TradingAPI.CancelAllOrders import endpoint_info as delete_all_orders
from API.TradingAPI.CancelMutipleOrders import endpoint_info as delete_multiple_orders
from API.TradingAPI.CancelOrder import endpoint_info as delete_order
from API.TradingAPI.PlaceIOCOrder import endpoint_info as post_ioc_order
from API.TradingAPI.PlaceLimitOrder import endpoint_info as post_limit_order
from API.TradingAPI.PlaceMarketOrder import endpoint_info as post_market_order
from API.TradingAPI.PlaceMultipleLimitOrders import endpoint_info as post_multiple_limit_orders
from API.TradingAPI.PlaceStopLimitOrder import endpoint_info as post_stop_limit_order


class Coinex:
    def __init__(self, access_id=None, secret_key=None,
                 check_params=True, param_err_msg="exception", response_format='json'):
        self._configs = {
            "access_id": access_id,
            "secret_key": secret_key,
            "check_params": check_params,
            "param_err_msg": param_err_msg,
            "response_format": response_format
        }
        self._argument_check(self._configs)

    def config(self, access_id=0, secret_key=0,
               check_params=0, param_err_msg=0, response_format=0):
        # Argument will be ignored if it's 0
        new_configs = {"access_id": access_id if access_id != 0 else self._configs["access_id"],
                       "secret_key": secret_key if secret_key != 0 else self._configs["secret_key"],
                       "check_params": check_params if check_params != 0 else self._configs["check_params"],
                       "param_err_msg": param_err_msg if param_err_msg != 0 else self._configs["param_err_msg"],
                       "response_format": response_format if response_format != 0 else self._configs["response_format"]}
        self._argument_check(new_configs)

    def _argument_check(self, configs):
        if type(configs["access_id"]) is str or configs["access_id"] is None:
            self._configs["access_id"] = configs["access_id"]
        else:
            raise ArgumentTypeErr("access_id", "string")

        if type(configs["secret_key"]) == str or configs["secret_key"] is None:
            self._configs["secret_key"] = configs["secret_key"]
        else:
            raise ArgumentTypeErr("secret_key", "string")

        if configs["check_params"] in ["all", "trv", "t", "r", "v", "tr", "tv", "rt", "rv", "vt", "vr", True, False]:
            self._configs["check_params"] = configs["check_params"]
        else:
            raise ArgumentValueErr("check_params", "be 'all', any combination of 'trv' or True/False")

        if configs["param_err_msg"] in ["exception", "print", None]:
            self._configs["param_err_msg"] = configs["param_err_msg"]
        else:
            raise ArgumentValueErr("param_err_msg", "be one of the following: 'exception', 'print', None")

        if configs["response_format"] in ["json", "simplified"]:
            self._configs['response_format'] = configs["response_format"]
        else:
            raise ArgumentValueErr("response_format", "be one of the following: 'json', 'simplified'")

    def acquire_asset_config(self, coin_type=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_asset_config
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_currency_rate(self):
        params = {}
        endpoint_info = get_currency_rate
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_site_maintain_info(self):
        params = {}
        endpoint_info = get_site_maintain_info
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_credit_account_info(self):
        params = {}
        endpoint_info = get_credit_account_info
        return APICall(self._configs, endpoint_info, params).get_result()

    def cancel_withdrawal(self, coin_withdraw_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = delete_withdrawal
        return APICall(self._configs, endpoint_info, params).get_result()

    def generate_deposit_address(self, coin_type=None, smart_contract_name=None):
        params = locals()
        params.pop('self')
        endpoint_info = put_deposit_address
        return APICall(self._configs, endpoint_info, params).get_result()

    def get_deposit_address(self, coin_type, smart_contract_name=None, is_split=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_deposit_addres
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_account_info(self):
        params = {}
        endpoint_info = get_account_info
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_deposit_list(self, coin_type=None, status=None, page=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_deposit_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_investment_transfer_history(self, op_type=None, asset=None, start_time=None, end_time=None,
                                            page=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_investment_transfer_history
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_margin_account_market_info(self):
        params = {}
        endpoint_info = get_margin_account_market_info
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_margin_transfer_history(self, market=None, transfer_type=None, asset=None, start_time=None,
                                        end_time=None, page=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_margin_transfer_history
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_market_fee(self, market=None, business_type=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_market_fee
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_perpetual_transfer_history(self, transfer_type=None, asset=None, start_time=None, end_time=None,
                                           page=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_perpetual_transfer_history
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_sub_account_balance(self, sub_user_name=None, coin_type=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_subaccount_balance
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_sub_account_balance_history(self, sub_user_name=None, coin_type=None, page=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_subaccount_balance_history
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_withdrawal_list(self, coin_type=None, coin_withdraw_id=None, page=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_withdrawal_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def submit_withdrawal_order(self, coin_type=None, smart_contract_name=None,
                                coin_address=None, transfer_method=None, actual_amount=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_withdrawal_order
        return APICall(self._configs, endpoint_info, params).get_result()

    def transfer_between_mainacc_and_marginacc(self, from_account=None, to_account=None, coin_type=None, amount=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_transfer_main_margin
        return APICall(self._configs, endpoint_info, params).get_result()

    def transfer_between_mainacc_and_subacc(self, transfer_account=None, transfer_side=None,
                                            coin_type=None, amount=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_transfer_main_sub
        return APICall(self._configs, endpoint_info, params).get_result()

    def balance_transfer(self, transfer_side=None, coin_type=None, amount=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_balance_transfer
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_loan_list(self, market=None, status=None, page=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_loan_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_margin_account_settings(self, market=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_margin_account_settings
        return APICall(self._configs, endpoint_info, params).get_result()

    def inquire_margin_account_info(self, market=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_margin_account_info
        return APICall(self._configs, endpoint_info, params).get_result()

    def place_flat(self, market=None, coin_type=None, amount=None, loan_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_flat
        return APICall(self._configs, endpoint_info, params).get_result()

    def place_loan(self, market=None, coin_type=None, amount=None, renew=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_loan
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_amm_market_list(self):
        params = {}
        endpoint_info = get_amm_market_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_k_line_data(self, market=None, type=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_kline_data
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_latest_transaction_data(self, market=None, last_id=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_latest_transaction_data
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_market_depth(self, market=None, merge=None, limit=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_market_depth
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_single_market_information(self, market=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_single_market_information
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_market_information(self):
        params = {}
        endpoint_info = get_market_information
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_market_list(self):
        params = {}
        endpoint_info = get_market_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_market_statistics(self, market=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_market_statistics
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_all_markets_statistics(self):
        params = {}
        endpoint_info = get_all_markets_statistics
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_executed_order_detail(self, id=None, page=None, limit=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_executed_order_detail
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_executed_order_list(self, market=None, page=None, limit=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_executed_order_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_executed_stop_order_list(self, market=None, page=None, limit=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_executed_stop_order_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_multiple_orders_status(self, batch_ids=None, market=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_multiple_orders_status
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_order_status(self, id=None, market=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_order_status
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_unexecuted_order_list(self, market=None, type=None, page=None, limit=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_unexecuted_order_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_unexecuted_stop_order_list(self, market=None, type=None, page=None, limit=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_unexecuted_stop_order_list
        return APICall(self._configs, endpoint_info, params).get_result()

    def acquire_user_deals(self, market=None, page=None, limit=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = get_user_deals
        return APICall(self._configs, endpoint_info, params).get_result()

    def cancel_all_orders(self, account_id=None, market=None):
        params = locals()
        params.pop('self')
        endpoint_info = delete_all_orders
        return APICall(self._configs, endpoint_info, params).get_result()

    def cancel_multiple_orders(self, batch_ids=None, market=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = delete_multiple_orders
        return APICall(self._configs, endpoint_info, params).get_result()

    def cancel_order(self, id=None, market=None, type=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = delete_order
        return APICall(self._configs, endpoint_info, params).get_result()

    def place_ioc_order(self, market=None, type=None, amount=None, price=None, source_id=None, account_id=None,
                        client_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_ioc_order
        return APICall(self._configs, endpoint_info, params).get_result()

    def place_limit_order(self, market=None, type=None, amount=None, price=None, source_id=None, option=None,
                          account_id=None, client_id=None, hide=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_limit_order
        return APICall(self._configs, endpoint_info, params).get_result()

    def place_market_order(self, market=None, type=None, amount=None, account_id=None, client_id=None, source_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_market_order
        return APICall(self._configs, endpoint_info, params).get_result()

    def place_multiple_limit_orders(self, batch_orders=None, market=None, type=None, amount=None, price=None,
                                    source_id=None, account_id=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_multiple_limit_orders
        return APICall(self._configs, endpoint_info, params).get_result()

    def place_stop_limit_order(self, market=None, type=None, amount=None, price=None, stop_price=None, source_id=None,
                               option=None, account_id=None, client_id=None, hide=None):
        params = locals()
        params.pop('self')
        endpoint_info = post_stop_limit_order
        return APICall(self._configs, endpoint_info, params).get_result()

