from django.db import models
from backend.models import Patient, TimeBasedModel

class MultiOrganFailure(TimeBasedModel):
    class Meta:
        verbose_name = "Запись Полиорганной недостаточноти"
        verbose_name_plural = "Записи Полиорганной недостаточноти"
        
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="mof_collection", verbose_name="Пациент")
    sofa = models.IntegerField("Баллы SOFA")
    
