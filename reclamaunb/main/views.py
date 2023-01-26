from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView
from .forms import SecurityReportForm
from .models import SecurityReportModel

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'main/home.html'

class RedirectReportView(TemplateView):
    template_name = 'main/redirect_report.html'

class SecurityReportView(CreateView):
    template_name = 'main/security_report.html'
    form_class = SecurityReportForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:home')

class ReportListView(ListView):
    template_name = 'main/report_list.html'
    model = SecurityReportModel

    def get_queryset(self):
        return SecurityReportModel.objects.all()