from ..utils.api_request_handler import ApiRequestHandler

def fetch_manufacturer_info(params):
    apiRequestHandler = ApiRequestHandler('http://apis.data.go.kr')
    endpoint = '1471000/MdlpMnfcturPrmisnInfoService01/getMdlpMnfcturPrmisnList01'
    data = apiRequestHandler.send_api_request(endpoint = endpoint, params = params)
    return data
