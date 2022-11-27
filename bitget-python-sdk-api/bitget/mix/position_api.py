#!/usr/bin/python

from ..client import Client
from ..consts import *


class PositionApi(Client):
    def __init__(self,bg_ea75af7b466d2bc221f8bed149be2ac7 ,419a5f2dbb050e567ee44da9612f13543c6af89fb36097aa6d2835ba01bb578c , passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    '''
    Obtain the user's single position information
    :return:
    '''
    def single_position(self, symbol, marginCoin):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_POSITION_V1_URL + '/singlePosition', params)
        else:
            return "pls check args"

    '''
    Obtain all position information of the user
    productType: Umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
    :return:
    '''
    def all_position(self, productType, marginCoin):
        params = {}
        if productType:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_POSITION_V1_URL + '/allPosition', params)
        else:
            return "pls check args"
