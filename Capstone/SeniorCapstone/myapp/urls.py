#Import the url mapping from the project folder
from django.urls import path

# Import all the views
from . import views


# Create the Url patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('stats/', views.statistics, name = 'state-demographic-list'),
    path('visualstats/', views.StatisticsData().as_view(), name = 'visual-stats'),
    path('history/', views.history, name = 'history')
]