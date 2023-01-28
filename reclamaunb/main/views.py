from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.db.models import Count
from .forms import SecurityReportForm
from .models import SecurityReportModel, AcademicUnitModel


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

class ReportDetailView(DetailView):
    pk_url_kwarg = 'pk'
    template_name = 'main/report_detail.html'
    model = SecurityReportModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ReportChartsView(TemplateView):
    template_name = 'main/report_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the names of the top 3 buildings with the most reports
        context["buildings"] = [x.abbreviation for x in AcademicUnitModel.objects.annotate(num_reports=Count('securityreportmodel')).order_by('-num_reports')[:3]]

        # Get the number of reports for each of the top 3 buildings
        context["num_reports"] = [x.num_reports for x in AcademicUnitModel.objects.annotate(num_reports=Count('securityreportmodel')).order_by('-num_reports')[:3]]
       
        return context