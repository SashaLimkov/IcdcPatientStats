from django.db import models
from backend.models import Patient, TimeBasedModel

class CardiovascularSystem(TimeBasedModel):
    class Meta:
        verbose_name = "Запись сердечно-сосудистой системы "
        verbose_name_plural = "Записи сердечно-сосудистой системы"
        
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="cs_collection")
    pulse = models.IntegerField("пульс в минуту")
    chss = models.IntegerField("ЧСС в минуту")
    ad_up = models.IntegerField("АД верх")
    ad_down = models.IntegerField("АД низ")

    @property
    def pretty_ad(self):
        return f"{self.ad_up}/{self.ad_down} мм. рт. ст."