from django.urls import path, include
from .views import extractProductInfo

urlpatterns = [
    path("url", extractProductInfo),
]