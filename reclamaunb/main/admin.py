from django.contrib import admin
from .models import AcademicUnitModel, SecurityReportModel

# Register your models here.
admin.site.register(AcademicUnitModel)
admin.site.register(SecurityReportModel)