from rest_framework import serializers

class ManufacturerApiParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, source='pageNo')
    per_page = serializers.IntegerField(required=False, source='numOfRows')
    company_name = serializers.CharField(required=False, source='Entrps')
    industry_type = serializers.CharField(required=False, source='Induty_type')
    permit_date = serializers.CharField(required=False, source='Prmisn_dt')
    license_number = serializers.CharField(required=False, source='Meddev_entp_no')

class ProductListApiParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, source='pageNo')
    per_page = serializers.IntegerField(required=False, source='numOfRows')
    item_name = serializers.CharField(required=False, source='PRDLST_NM')
