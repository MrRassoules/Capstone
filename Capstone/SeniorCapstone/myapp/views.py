from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from myapp.models import StateDemographic
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

    
    