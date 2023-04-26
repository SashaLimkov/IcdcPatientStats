from django.db import models
from IcdcPatientStat.backend.models import Patient, TimeBasedModel

class ImmuneSystem(TimeBasedModel):
    class Meta:
        verbose_name = "Запись имунной системы "
        verbose_name_plural = "Записи имунной системы"
        
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="is_collection")
    temperature = models.FloatField("Температуры в градусах Цельсия")
    description = models.CharField("Описание результатов", max_length=512)