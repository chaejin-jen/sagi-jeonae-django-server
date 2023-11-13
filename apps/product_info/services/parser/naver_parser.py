from .parser_factory import BaseParser, regist_site

import json

from ...utils.url_fetcher import fetch_page_contents

@regist_site('smartstore.naver.com')
@regist_site('m.smartstore.naver.com')
@regist_site('www.smartstore.naver.com')
class NaverParser(BaseParser):
    def parse(self, url):
        try:
            contents = fetch_page_contents(url, BaseParser.get_headers())
            return NaverParser._extract_product_info(contents)
        except ValueError as e:
            print(f"Error in parsing: {e}")

    def _extract_product_info(contents):
        try:
            json_data = NaverParser._extract_json_data(contents)
            data = json.loads(json_data)
            product_info = data.get('product', {}).get('A', {}).get('productInfoProvidedNoticeView', {}).get('basic', {})
            return product_info
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to parse JSON: {e}")

    def _extract_json_data(contents):
        start_marker = 'window.__PRELOADED_STATE__='
        end_marker = '</script>'
        start_index = contents.find(start_marker) + len(start_marker)
        end_index = contents.find(end_marker, start_index)
        json_data = contents[start_index:end_index]
        return json_data

