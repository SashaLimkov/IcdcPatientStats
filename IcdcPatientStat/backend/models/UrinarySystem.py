from django.db import models
from backend.models import Patient, TimeBasedModel

class UrinarySystem(TimeBasedModel):
    class Meta:
        verbose_name = "Запись центральной нервной системы"
        verbose_name_plural = "Записи центральной нервной системы"
        
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="urin_collection", verbose_name="Пациент")
    diurez = models.IntegerField("Суточный диурез")
    infuzyy = models.IntegerField("Инфузии")
