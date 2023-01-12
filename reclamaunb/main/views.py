from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'main/home.html'

class RedirectReportView(TemplateView):
    template_name = 'main/redirect_report.html'
