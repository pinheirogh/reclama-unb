from django.contrib import admin
from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dados/', HomePageView.as_view(), name='dados'),
    path('reclamacoes/', HomePageView.as_view(), name='reclamacoes'),
    path('reportar/', HomePageView.as_view(), name='reportar'),
]