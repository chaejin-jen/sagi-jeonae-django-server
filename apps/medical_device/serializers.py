from rest_framework import serializers

class ManufacturerApiParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, source='pageNo')
    per_page = serializers.IntegerField(required=False, source='numOfRows')
    company_name = serializers.CharField(required=False, source='Entrps')
    industry_type = serializers.CharField(required=False, source='Induty_type')
    permit_date = serializers.CharField(required=False, source='Prmisn_dt')
    license_number = serializers.CharField(required=False, source='Meddev_entp_no')

class ItemApiParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, source='pageNo')
    per_page = serializers.IntegerField(required=False, source='numOfRows')
    item_name = serializers.CharField(required=False, source='PRDLST_NM')

class ProductApiParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, source='pageNo')
    per_page = serializers.IntegerField(required=False, source='numOfRows')
    udidi_code = serializers.CharField(required=False, source='UDIDI_CD')
    item_name = serializers.CharField(required=False, source='PRDLST_NM')
    clsf_number = serializers.CharField(required=False, source='MDEQ_CLSF_NO')
    clsf__level = serializers.IntegerField(required=False, source='CLSF_NO_GRAD_CD')
    permit_number = serializers.CharField(required=False, source='PERMIT_NO')
    model_name = serializers.CharField(required=False, source='FOML_INFO')
    company_name = serializers.CharField(required=False, source='MNFT_IPRT_ENTP_NM')
