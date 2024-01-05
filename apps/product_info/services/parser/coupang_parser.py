from .parser_factory import BaseParser, regist_site

from urllib.parse import urlparse
from urllib.request import urlopen, Request

import json

from ...utils.url_fetcher import fetch_page_contents, fetch_response_url

@regist_site('coupang.com')
@regist_site('m.coupang.com')
@regist_site('www.coupang.com')
@regist_site('link.coupang.com')
class CoupangParser(BaseParser):
    def parse(self, url):
        try:
            url = CoupangParser._transform_to_data_url(url)
            contents = fetch_page_contents(url, BaseParser.get_headers())
            return CoupangParser._extract_product_info(contents)
        except ValueError as e:
            print(f"Error in parsing: {e}")

    def _transform_to_data_url(page_url):
        if 'link.coupang.com' in page_url:
            page_url = fetch_response_url(page_url, BaseParser.get_headers())
        parsed_url = urlparse(page_url)
        path = parsed_url.path

        query_params = dict(pair.split('=') for pair in parsed_url.query.split('&'))
        print(f'\n\n query_params {query_params}')

        new_path = f"{path}/items/{query_params['itemId']}/vendoritems/{query_params['vendorItemId']}"

        data_url = f"{parsed_url.scheme}://{parsed_url.netloc}{new_path}"
        return data_url

    def _extract_product_info(json_data):
        data = json.loads(json_data)

        product_info = {}
        for certification in data.get("vendorItemCertifications", []):
            product_info[certification['name']] = certification['certificationNo']

        for essential in data.get("essentials", []):
            product_info[essential['title']] = essential['description']

        return product_info
