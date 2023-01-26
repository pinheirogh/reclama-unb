from django.contrib import admin
from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dados/', HomePageView.as_view(), name='dados'),
    path('reclamacoes/', ReportListView.as_view(), name='reclamacoes'),
    path('reclamacoes/<int:pk>/', ReportDetailView.as_view(), name='detalhe_reclamacao'),
    path('reportar/', RedirectReportView.as_view(), name='reportar'),
    path('reportar/seguranca', SecurityReportView.as_view(), name='reportar_seguranca'),
    path('reportar/infraestrutura', RedirectReportView.as_view(), name='reportar_infraestrutura'),    
]