from django.db import models
from backend.models import Patient, TimeBasedModel


class RespiratorySystem(TimeBasedModel):
    class Meta:
        verbose_name = "Запись дыхательной системы"
        verbose_name_plural = "Записи дыхательной системы"

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="rs_collection",
        verbose_name="Пациент",
    )
    system_type = models.CharField("Тип дыхания", max_length=255)
    ventilation_type = models.CharField(
        "Режим вентиляции", max_length=255, blank=True, null=True
    )
    do = models.IntegerField("ДО", blank=True, null=True)
    chd = models.IntegerField("ЧД")
    FiO2 = models.IntegerField("FiO2 %", blank=True, null=True)
    peep = models.IntegerField("PEEP", blank=True, null=True)
    saturation = models.IntegerField("Сатурация %")
