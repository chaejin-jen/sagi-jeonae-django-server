from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_501_NOT_IMPLEMENTED

from .serializers import ManufacturerApiParamsSerializer, ProductApiParamsSerializer
from .services.manufacturer_info import fetch_manufacturer_info
from .services.product_info import fetch_product_info

# Create your views here.
@api_view(['GET'])
def getManufacturerInfo(request):
    serializer = ManufacturerApiParamsSerializer(data=request.GET)

    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)

    params = serializer.validated_data
    manufacturer_data = fetch_manufacturer_info(params)
    try:
        if manufacturer_data:
            return Response(manufacturer_data)
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
    manufacturer_data = fetch_product_info(params)
    try:
        if manufacturer_data:
            return Response(manufacturer_data)
        else:
            return Response({"error": "정보를 가져올 수 없습니다."}, status=HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response({"error": f"지원하지 않는 사이트입니다. ({e})"}, status=HTTP_501_NOT_IMPLEMENTED)
