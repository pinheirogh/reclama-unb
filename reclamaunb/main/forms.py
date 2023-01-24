from django.forms import ModelForm
from .models import SecurityReportModel

class SecurityReportForm(ModelForm):

    class Meta:
        model = SecurityReportModel
        fields = '__all__'