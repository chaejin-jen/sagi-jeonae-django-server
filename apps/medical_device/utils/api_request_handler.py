from common.http_utils.http_request_handler import HttpRequestHandler

from .api_exceptions import *

import urllib.parse
import json
import os
from dotenv import load_dotenv

class ApiRequestHandler(HttpRequestHandler):
    def __init__(self, host, timeout=10, dotenv_path = '.env', service_key_name = 'DATA_GO_SERVICE_KEY'):
        super().__init__(timeout)
        self.host = host
        self.dotenv_path = dotenv_path
        self.service_key_name = service_key_name

    def send_api_request(self, endpoint, params=None, method='GET'):
        url = f"{self.host}/{endpoint}?{self._prepare_request_data(params)}"
        response = self.send_request(url, method=method)
        print(f'\n\n========\n{response}')
        response_data = json.loads(response)
        header = response_data.get('header', {})
        body = response_data.get('body', {})
        return body if header.get('resultCode') == '00' else self.handle_api_error(header)

    def _prepare_request_data(self, params : {str:str}):
        load_dotenv(self.dotenv_path)
        params['serviceKey'] = os.getenv(self.service_key_name)
        params['type'] = 'json'
        return urllib.parse.urlencode(params)

    def handle_api_error(self, error_response):
        # API 오류 응답 처리
        error_code = error_response.get('resultCode', None)
        error_code = int(error_code) if error_code else error_code
        error_msg = error_response.get('resultMsg', None)

        if error_code == 1:
            # 어플리케이션 에러
            raise ApplicationError(error_msg)
        elif error_code == 4:
            # HTTP 에러
            raise HttpError(error_msg)
        elif error_code == 12:
            # 해당 오픈 API 서비스가 없거나 폐기됨
            raise NoOpenApiServiceError(error_msg)
        elif error_code == 20:
            # 서비스 접근 거부
            raise ServiceAccessDeniedError(error_msg)
        elif error_code == 22:
            # 서비스 요청 제한 횟수 초과 에러
            raise LimitedNumberOfServiceRequestsExceedsError(error_msg)
        elif error_code == 30:
            # 등록되지 않은 서비스키
            raise ServiceKeyNotRegisteredError(error_msg)
        elif error_code == 31:
            # 활용 기간 만료
            raise DeadlineHasExpiredError(error_msg)
        elif error_code == 32:
            # 등록되지 않은 IP
            raise UnregisteredIpError(error_msg)
        elif error_code == 99:
            # 기타 에러
            raise UnknownError(error_msg)
        else:
            # 알 수 없는 오류 코드
            raise ValueError(f"Unknown error code: {error_code}, Message: {error_msg}")

