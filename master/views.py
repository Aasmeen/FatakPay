from crm.models import CRMPil
from master.models import MASSlm
from master.serializers import MasterSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class MasterAPI(ModelViewSet):
    serializer_class = MasterSerializer
    queryset = MASSlm.objects.all()
