from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_501_NOT_IMPLEMENTED
from rest_framework.decorators import api_view

from urllib.parse import urlparse
from urllib.parse import unquote
from .services.parser.parser_factory import ParserFactory

@api_view(['GET'])
def extractProductInfo(request):
    url = request.GET.get('encoded_url', None)
    if not url:
        return Response({"error": "URL 파라미터가 필요합니다."}, status=HTTP_400_BAD_REQUEST)
    parsed_url = urlparse(url)
    site = parsed_url.netloc

    try:
        parser = ParserFactory.get_parser(site)
        if parser:
            url = unquote(url)
            product_info = parser.parse(url)
            if product_info:
                return Response(product_info)
            else:
                return Response({"error": "정보를 가져올 수 없습니다."}, status=HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response({"error": f"지원하지 않는 사이트입니다. ({e})"}, status=HTTP_501_NOT_IMPLEMENTED)
