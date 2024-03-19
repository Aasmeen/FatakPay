import calendar

from django.db.models import F, Sum
from django.db.models.functions import ExtractMonth
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from crm.models import CRMLed, CRMOpp, CRMPil
from crm.serializers import CRMSerializer
# Create your views here.

class CRMAPI(ModelViewSet):
    serializer_class = CRMSerializer
    queryset = CRMLed.objects.all()

class GetForecast(APIView):

    def get(self, request, *args, **kwargs):
        probability_percent = CRMPil.objects.filter(is_active=True)
        if probability_percent.exists():
            probability_percent_val = probability_percent.last().probability_percent
            filtered_opportunities = CRMOpp.objects.filter(closed_on__isnull=True)
            filtered_opportunities = filtered_opportunities.annotate(forecast_amount=F('amount') * probability_percent_val, month=ExtractMonth('target_date'))
            filtered_opportunities = filtered_opportunities.values('month').annotate(forecast=Sum('forecast_amount')).values('month', 'forecast')
        res = []
        for opportunities in filtered_opportunities:
            res.append({'month': calendar.month_name[opportunities['month']], 'forecast': opportunities['forecast']})
        return Response(res)
