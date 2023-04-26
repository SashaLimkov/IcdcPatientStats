from django.db import models

from backend.models import TimeBasedModel


class Patient(TimeBasedModel):
    class Meta:
        verbose_name = "Пациента"
        verbose_name_plural = "Пациенты"

    ema = models.CharField("ЭМА", max_length=255)
    empz = models.CharField("ЭМПЗ", max_length=255)
    patient_id = models.CharField("№", max_length=255, primary_key=True)
    ilness_history_num = models.CharField("ИБ №")
    fio = models.CharField("ФИО", max_length=1000)

    def __str__(self) -> str:
        return self.fio
