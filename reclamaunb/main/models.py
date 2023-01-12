from django.db import models

# Create your models here.
class ReportModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class AcademicUnit(models.Model):
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
    building = models.ForeignKey(AcademicUnit, on_delete=models.CASCADE)
