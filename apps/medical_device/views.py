from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_501_NOT_IMPLEMENTED

from .serializers import ManufacturerApiParamsSerializer, ProductApiParamsSerializer
from .services.manufacturer_info import fetch_manufacturer_info
from .services.product_info import fetch_product_info

from common.data.formatters.data_go_response_formatter import DataGoResponseFormatter
from .data.formatters.mappings import medical_device_manufacturer_mapping, medical_device_product_mapping

# Create your views here.
@api_view(['GET'])
def getManufacturerInfo(request):
    serializer = ManufacturerApiParamsSerializer(data=request.GET)

    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)

    params = serializer.validated_data
    manufacturer_response = fetch_manufacturer_info(params)
    try:
        if manufacturer_response:
            manufacturer_formatter = DataGoResponseFormatter(medical_device_manufacturer_mapping)

            return Response(manufacturer_formatter.format_response(manufacturer_response))
        else:
            return Response({"error": "정보를 가져올 수 없습니다."}, status=HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response({"error": f"지원하지 않는 사이트입니다. ({e})"}, status=HTTP_501_NOT_IMPLEMENTED)

@api_view(['GET'])
def getProductInfo(request):
    serializer = ProductApiParamsSerializer(data=request.GET)

    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)

    params = serializer.validated_data
    print(params)
    product_response = fetch_product_info(params)
    try:
        if product_response:
            product_formatter = DataGoResponseFormatter(medical_device_product_mapping)

            return Response(product_formatter.format_response(product_response))
        else:
            return Response({"error": "정보를 가져올 수 없습니다."}, status=HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response({"error": f"지원하지 않는 사이트입니다. ({e})"}, status=HTTP_501_NOT_IMPLEMENTED)
