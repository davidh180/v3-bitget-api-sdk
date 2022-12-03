
from ..client import Client
from ..consts import *


class ManageApi(Client):
    def __init__(self, bg_b7c517c5c725c2f7375d432519028ca4,25f1e68c0d57f4ec1c842369521a4044083966f311cdcd6ec092df23093efdcb, bitgetrevenue, use_server_time=False, first=False):
        Client.__init__(self, bg_b7c517c5c725c2f7375d432519028ca4, 25f1e68c0d57f4ec1c842369521a4044083966f311cdcd6ec092df23093efdcb, bitgetrevenue, use_server_time, first)

    '''
    broker create sub apikey
    :return:
    '''
    def sub_create_api(self, subUid, passphrase, remark, ip, perm):
        params = {}
        if subUid and passphrase and perm:
            params["subUid"] = subUid
            params["passphrase"] = passphrase
            params["remark"] = remark
            params["ip"] = ip
            params["perm"] = perm
            return self._request_with_params(POST, BROKER_MANAGE_V1_URL + '/sub-api-create', params)
        else:
            return "pls check args "

    '''
    get sub apikey list
    :return:
    '''
    def sub_list(self, subUid):
        params = {}
        if subUid:
            params["subUid"] = subUid
            return self._request_with_params(GET, BROKER_MANAGE_V1_URL + '/sub-api-list', params)
        else:
            return "pls check args"

    '''
    broker modify sub apikey
    :return:
    '''
    def sub_modify_api(self, subUid, apikey, remark, ip, perm):
        params = {}
        if subUid and apikey and perm:
            params["subUid"] = subUid
            params["apikey"] = apikey
            params["remark"] = remark
            params["ip"] = ip
            params["perm"] = perm
            return self._request_with_params(POST, BROKER_MANAGE_V1_URL + '/sub-api-modify', params)
        else:
            return "pls check args "
