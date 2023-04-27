from django.db import models
from backend.models import Patient, TimeBasedModel


class CentralNervousSystem(TimeBasedModel):
    class Meta:
        verbose_name = "Запись центральной нервной системы"
        verbose_name_plural = "Записи центральной нервной системы"

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="cns_collection",
        verbose_name="Пациент",
    )
    points = models.IntegerField("Результаты оценки по шкале ком Глазго")
    description = models.CharField("Описание результатов", max_length=512)
