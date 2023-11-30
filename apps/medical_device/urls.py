from django.urls import path, include
from .views import getManufacturerInfo, getProductInfo

urlpatterns = [
    path("manufacturer", getManufacturerInfo),
    path("product", getProductInfo),
]
