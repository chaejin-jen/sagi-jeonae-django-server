from ..utils.api_request_handler import ApiRequestHandler

def fetch_item_info(params):
    apiRequestHandler = ApiRequestHandler('http://apis.data.go.kr')
    endpoint = '1471000/MdeqPrdlstInfoService02/getMdeqPrdlstInfoInq02'
    data = apiRequestHandler.send_api_request(endpoint = endpoint, params = params)
    return data

def fetch_product_info(params):
    apiRequestHandler = ApiRequestHandler('http://apis.data.go.kr')
    endpoint = '1471000/MdeqStdCdPrdtInfoService03/getMdeqStdCdPrdtInfoInq03'
    data = apiRequestHandler.send_api_request(endpoint = endpoint, params = params)
    return data
