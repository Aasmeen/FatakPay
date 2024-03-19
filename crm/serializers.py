from crm.models import CRMLed
from rest_framework.serializers import ModelSerializer

class CRMSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CRMLed
