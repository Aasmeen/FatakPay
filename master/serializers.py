from master.models import MASSlm
from rest_framework.serializers import ModelSerializer

class MasterSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MASSlm
