from rest_framework import serializers

class ManufacturerApiParamsSerializer(serializers.Serializer):
    Entrps = serializers.CharField(required=False)
    Induty_type = serializers.CharField(required=False)
    Prmisn_dt = serializers.CharField(required=False)
    pageNo = serializers.IntegerField(required=False)
    numOfRows = serializers.IntegerField(required=False)
    Meddev_entp_no = serializers.CharField(required=False)

class ProductApiParamsSerializer(serializers.Serializer):
    pageNo = serializers.IntegerField(required=False)
    numOfRows = serializers.IntegerField(required=False)
    PRDLST_NM = serializers.CharField(required=False)
