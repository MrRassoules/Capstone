from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from myapp.models import StateDemographic
from django.core import serializers
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def statistics(request):
    state_demographics = StateDemographic.objects.all()
    context = {
        'state_demographics' : state_demographics
    }
    # Get the selected state
    if request.method == 'POST':
        selected_state = state_demographics.filter(state = request.POST.get('state_list')).first()
        context.update({
            'selected_state' : selected_state
        })
        
    # Render the page
    return render(request, 'statedemographic_list.html', context)

class StateDemographicListView():
    model = StateDemographic
    template_name = "statedemographic_list.html"

    
# Test Stats view
class StatisticsData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        state_information = StateDemographic.objects.all()
        labels = state_information.values_list("state", flat=True)
        chartdata = state_information.values_list("black_median_income", flat=True)
        data = {
            "labels" : labels,
            "chartdata": chartdata,
        }
        return Response(data)