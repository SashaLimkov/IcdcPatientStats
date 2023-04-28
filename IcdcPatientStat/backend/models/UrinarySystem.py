from django.db import models
from backend.models import Patient, TimeBasedModel


class UrinarySystem(TimeBasedModel):
    class Meta:
        verbose_name = "Запись Мочевыделительной системы"
        verbose_name_plural = "Записи Мочевыделительной системы"

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="urin_collection",
        verbose_name="Пациент",
        to_field="patient_id",
    )
    diurez = models.IntegerField("Суточный диурез")
    infuzyy = models.IntegerField("Инфузии")
