from django.db import models

# Create your models here.
class ReportModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' (' + self.date.strftime('%d/%m/%Y') + ')'

    class Meta:
        abstract = True

class AcademicUnitModel(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name

class SecurityReportModel(ReportModel):
    SPECIFIC_LOCATION_CHOICES = (
        ('Entrada', 'Entrada'),
        ('Saida', 'Saida'),
        ('Corredor', 'Corredor'),
        ('Banheiro', 'Banheiro'),
        ('Sala de Aula', 'Sala de Aula'),
        ('Laboratorio', 'Laboratorio'),
        ('Estacionamento', 'Estacionamento'),
        ('Frente', 'Frente'),
        ('Atrás', 'Atrás'),
        ('Lado', 'Lado'),
        ('Outro', 'Outro'),
    )
    specific_location = models.CharField(max_length=100, choices=SPECIFIC_LOCATION_CHOICES)
    building = models.ForeignKey(AcademicUnitModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

    def is_securityreport(self):
        return True
